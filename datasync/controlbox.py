import logging
import time

from brewpi.connector.codecs.time import (
    BlockBufferCodec, TypeMappingCodec, DictionaryMappingCodec,
    BrewpiStateCodec, BrewpiConstructorCodec, ScaledTimeCodec
)
from brewpi.protocol.factory import all_sniffers
from controlbox.connector_facade import ControllerDiscoveryFacade
from controlbox.protocol.io import determine_line_protocol
from controlbox.controller import Controlbox
from controlbox.events import ControlboxEvents, ConnectorCodec, ConnectorEventVisitor
from controlbox.protocol.controlbox import ControlboxProtocolV1
from controlbox.connector.socketconn import TCPServerEndpoint

from .abstract import AbstractSyncher

LOGGER = logging.getLogger(__name__)


class BrewpiEvents(ConnectorEventVisitor):
    def __call__(self, event):
        print(type(event))
        LOGGER.info(event)


def sniffer(conduit):
    return determine_line_protocol(conduit, all_sniffers)


class ControlboxSyncher(AbstractSyncher):
    """
    A loop that syncs to the controller using Controlbox/Connector
    """
    discoveries = [
        ControllerDiscoveryFacade.build_serial_discovery(sniffer),
        ControllerDiscoveryFacade.build_tcp_server_discovery(sniffer, "brewpi", known_addresses=(TCPServerEndpoint('localhost', '127.0.0.1', 8332),)),
    ]

    def __init__(self):
        self.facade = ControllerDiscoveryFacade(self.discoveries)

        self.facade.manager.events.add(self._handle_connection_event) # connected?

    def _dump_device_info_events(self, connector, protocol: ControlboxProtocolV1):
        if not hasattr(protocol, 'controller'):
            controller = protocol.controller = Controlbox(connector)
            events = controller.events = ControlboxEvents(controller, BrewpiConstructorCodec(), BrewpiStateCodec())
            events.listeners.add(BrewpiEvents())
        else:
            events = protocol.controller.events

        # todo - would be good if the system itself described the type as part of the read response
        # this makes the system more self-describing
        events.read_system([0], 0)
        events.read_system([1], 1)

    def _handle_connection(self, connection):
        connector = connection.connector
        if connector.connected:
            self._dump_device_info_events(connector, connector.protocol)
        LOGGER.debug("_handle_connection")

    def _handle_connection_event(self, event):
        """
        Callback when a controller (dis)appears
        """
        print(event.connector)
        LOGGER.debug("_handle_connection_event")


    def run(self):
        while True:
            LOGGER.debug("youpi")
            self.facade.update()

            for connection in self.facade.manager.connections.values():
                self._handle_connection(connection)

            time.sleep(1)
