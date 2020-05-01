from game.main import format_time
import pytest
import pygame as pg




def test_format_time():

    result = format_time(1234)
    assert result == "1.23"

