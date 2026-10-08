#
# This file is licensed under the Affero General Public License (AGPL) version 3.
#
# Copyright (C) 2026 Kreesty
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# See the GNU Affero General Public License for more details:
# <https://www.gnu.org/licenses/agpl-3.0.html>.

from typing import Any, TypeGuard

from synapse.types import JsonDict

from ._base import Config


# Directly from the mypy docs:
# https://typing.python.org/en/latest/spec/narrowing.html#typeguard
def is_str_list(val: Any, allow_empty: bool) -> TypeGuard[list[str]]:
    """
    Type-narrow a value to a list of strings (compatible with mypy).
    """
    if not isinstance(val, list):
        return False

    if len(val) == 0:
        return allow_empty
    return all(isinstance(x, str) for x in val)


class NotificationRoutingConfig(Config):
    section = "notification_routing"

    def read_config(self, config: JsonDict, **kwargs: Any) -> None:
        notification_routing_config = config.get("notification_routing") or {}
        self.enabled = notification_routing_config.get("enabled", True)
        self.mobile_app_ids = notification_routing_config.get("mobile_app_ids", [])
        self.suppress_when_online = notification_routing_config.get(
            "suppress_when_online", True
        )
