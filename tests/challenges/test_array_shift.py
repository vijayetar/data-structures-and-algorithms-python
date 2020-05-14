from ...dsa.challenges.array_shift.array_shift import insertShiftArray, removeAndShiftArray

def test_one():
  actual=insertShiftArray([1,2,3,4,5],6)
  expected = [1,2,3,6,4,5]
  assert actual == expected

def test_two():
  actual=insertShiftArray([1,2,3,4],5)
  expected = [1,2,5,3,4]
  assert actual == expected

def test_three():
  actual=insertShiftArray([1,2,3,4],"")
  expected = [1,2,'',3,4]
  assert actual == expected

def test_four():
  actual=insertShiftArray([1,2,3,4],[2,3])
  expected = [1,2,[2,3],3,4]
  assert actual == expected

def test_five():
    actual = removeAndShiftArray([1,2,3,4,5])
    expected = [1,2,4,5]
    assert actual == expected

def test_six():
    actual = removeAndShiftArray([1,2,3,4])
    expected = [1,2,4]
    assert actual == expected

def test_seven():
    actual = removeAndShiftArray([])
    expected = []
    assert actual == expected






