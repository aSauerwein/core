"""Adds config flow for Keba."""

import voluptuous as vol

from homeassistant.config_entries import ConfigFlow, ConfigFlowResult
from homeassistant.const import CONF_HOST
import homeassistant.helpers.config_validation as cv

from . import (
    CONF_FS,
    CONF_FS_FALLBACK,
    CONF_FS_INTERVAL,
    CONF_FS_PERSIST,
    CONF_FS_TIMEOUT,
    CONF_RFID,
    DOMAIN,
)


class KebaFlowHandler(ConfigFlow, domain=DOMAIN):
    """Config flow for Keba."""

    VERSION = 1
    MINOR_VERSION = 1

    async def async_step_user(self, user_input) -> ConfigFlowResult:
        if user_input is not None:
            return self.async_create_entry(title="Keba Wallbox", data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_HOST): str,
                    vol.Optional(CONF_RFID, default="00845500"): cv.string,
                    vol.Optional(CONF_FS, default=False): cv.boolean,
                    vol.Optional(CONF_FS_TIMEOUT, default=30): cv.positive_int,
                    vol.Optional(CONF_FS_FALLBACK, default=6): cv.positive_int,
                    vol.Optional(CONF_FS_PERSIST, default=0): cv.positive_int,
                    vol.Optional(CONF_FS_INTERVAL, default=5): cv.positive_int,
                }
            ),
        )
