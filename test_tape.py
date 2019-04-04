import pytest

from tape import Tape

def test_get_content_of_non_empty_tape():
    tape = Tape('B', ['a', 'b', 'X', 'B'], ['a', 'b'])
    assert tape.get_content() == 'a'

def test_get_content_of_empty_tape():
    tape = Tape('B', ['a', 'b', 'X', 'B'], [])
    assert tape.get_content() == 'B'

def test_get_content_of_non_empty_tape_at_start_with_head_moved_to_left():
    tape = Tape('B', ['a', 'b', 'X', 'B'], ['a', 'b'])
    tape.move_left()
    assert tape.get_content() == 'B'
    assert tape.position == 0

def test_get_content_of_non_empty_tape_with_head_moved_to_right_left():
    tape = Tape('B', ['a', 'b', 'X', 'B'], ['a', 'b'])
    tape.move_right()
    tape.move_left()
    assert tape.get_content() == 'a'

def test_get_content_of_non_empty_tape_with_head_moved_to_right():
    tape = Tape('B', ['a', 'b', 'X', 'B'], ['a', 'b'])
    tape.move_right()
    assert tape.get_content() == 'b'

def test_get_content_of_non_empty_tape_at_end_with_head_moved_to_right():
    tape = Tape('B', ['a', 'b', 'X', 'B'], ['a', 'b'])
    tape.move_right()
    tape.move_right()
    assert tape.get_content() == 'B'

def test_move_head_left():
    tape = Tape('B', ['a', 'b', 'X', 'B'], ['a', 'b'])
    tape.move_head('L')
    assert tape.get_content() == 'B'

def test_move_head_right():
    tape = Tape('B', ['a', 'b', 'X', 'B'], ['a', 'b'])
    tape.move_head('R')
    assert tape.get_content() == 'b'

def test_move_head_stay():
    tape = Tape('B', ['a', 'b', 'X', 'B'], ['a', 'b'])
    tape.move_head('S')
    assert tape.get_content() == 'a'

def test_move_head_right_left():
    tape = Tape('B', ['a', 'b', 'X', 'B'], ['a', 'b'])
    tape.move_head('R')
    tape.move_head('L')
    assert tape.get_content() == 'a'

def test_set_content_empty_tape():
    tape = Tape('B', ['a', 'b', 'X', 'B'], [])
    tape.set_content('a')
    assert tape.get_content() == 'a'

def test_set_content_empty_tape_left_left_right():
    tape = Tape('B', ['a', 'b', 'X', 'B'], [])
    tape.move_left() 
    tape.move_left() 
    tape.move_right()
    tape.set_content('a') 
    assert tape.get_content() == 'a'  
    assert tape.position == 1

def test_set_string_empty_tape_left_left_right_a():
    tape = Tape('B', ['a', 'b', 'X', 'B'], [])
    tape.move_left() 
    tape.move_left() 
    tape.move_right()
    tape.set_content('a') 
    assert "(['B', 'a'])@1" == str(tape)
