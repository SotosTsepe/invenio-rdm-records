# -*- coding: utf-8 -*-
#
# Copyright (C) 2023 CERN.
#
# Invenio-RDM-Records is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.
"""Record 'verified' system field."""

from invenio_records_resources.records.systemfields.calculated import CalculatedField


class IsVerifiedField(CalculatedField):
    """Systemfield for calculating whether or not the request is expired."""

    def __init__(self, key=None):
        """Constructor."""
        super().__init__(key=key, use_cache=False)

    def calculate(self, record):
        """Calculate the ``is_expired`` property of the request."""
        owner = record.access.owner
        if not owner:
            return False
        is_verified = (
            owner.resolve().verified_at is not None
        )  # TODO property is_verified in user
        return is_verified