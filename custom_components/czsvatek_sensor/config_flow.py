"""Config flow for CZ svátek senzor integration."""
from __future__ import annotations

from homeassistant import config_entries
from homeassistant.data_entry_flow import FlowResult

from .const import DOMAIN


class CZSvatekConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for CZ svátek senzor."""

    VERSION = 1

    async def async_step_user(self, user_input: dict | None = None) -> FlowResult:
        """Handle the initial (and only) step.

        No configuration is needed, so this only lets the user confirm
        adding the sensor and blocks a second instance.
        """
        if self._async_current_entries():
            return self.async_abort(reason="single_instance_allowed")

        if user_input is not None:
            return self.async_create_entry(title="CZ svátek", data={})

        return self.async_show_form(step_id="user")
