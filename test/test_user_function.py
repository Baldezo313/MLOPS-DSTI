import pytest
import io
import os
import sys
sys.path.insert(0, 'C:/Users/balde/Desktop/DSTI/Mlops/MLOPS-DSTI/src')

from user_functions import *


def test_email_with_user_input_no_at_sign(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('baldezo.nokia.com'))
    assert get_email_from_input() is None


def test_email_with_user_input_no_dot(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('baldezo@nokiacom'))
    assert get_email_from_input() is None


def test_email_with_user_input_correct(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('baldezo@nokia.com'))
    assert get_email_from_input() == 'baldezo@nokia.com'


def test_user_name_empty_string(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO(''))
    assert get_user_name_from_input() is None


def test_user_name_with_space(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('bal de zo'))
    assert get_user_name_from_input() is None


def test_user_name_correct(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('baldezo'))
    assert get_user_name_from_input() == "baldezo"
