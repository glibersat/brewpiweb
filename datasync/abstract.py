from multimethod import multimethod, DispatchError

from django.db import models

from device.models import Device


class AbstractSyncher:
    """
    Abstract base class for writing new Model Synchronizers.
    FIXME This need to be reworked!
    """
    (PROTO_ONEWIRE) = range(0, 1)

    def read_sensor_states(self) -> bool:
        """
        Refresh and read state devices from the Controller
        """
        raise NotImplementedError

    def update_controller_model(self, save=False) -> bool:
        """
        Update the controller model and its devices
        """
        raise NotImplementedError

    def _update_installed_device_model(self, aDeviceClass, aController, slot_id, data) -> Device:
        """
        Given a slot and a Device class, create and/or update state
        """
        device = self._get_or_make_installed_device(aDeviceClass,
                                                    aController,
                                                    slot_id)

        try:
            self._update_model(device, data)
        except DispatchError:
            print("{0} Model not supported, skipping update.".format(type(device)))
            return None

        return device

    def _get_or_make_installed_device(self, aDeviceClass, aController, slot_id) -> Device:
        """
        Lookup an already installed device in the database.
        If none is found, create it in memory. Device needs to be saved manually.
        """
        need_create = False
        try:
            device = Device.objects.get(controller=aController, slot=slot_id)
            if not isinstance(device, aDeviceClass):
                # We have a bogus Device type for this slot_id, unassign it
                self._uninstall_device(device)
                device.save()

                need_create = True
        except Device.DoesNotExist:
            need_create = True

        if need_create:
            device = aDeviceClass(controller=aController, slot=slot_id)

        return device

    def _uninstall_device(self, aDevice):
        """
        Uninstall a given device on the model side
        """
        aDevice.slot_id = None

    def _make_uri(self, protocol, address) -> str:
        """
        Construct a URI from a given protocol and address
        """
        prefix = {AbstractSyncher.PROTO_ONEWIRE: 'onewire'}[protocol]

        return "{0}://{1}".format(prefix, address)

    @multimethod(models.Model, dict)
    def _update_model(aModel, data):
        """
        Update the fields of a given Model
        """
        raise NotImplementedError
