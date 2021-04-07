# -*- coding:utf-8 -*-

from .fakeclient import FakeClient


def get_fakeclient() -> FakeClient:
    return FakeClient()
