def is_palindrom(x):
  """
    :type x: int
    :rtype: bool
  """
  if x < 0:
    return False
  orginal = x
  reversed_num = 0
  while x > 0:
    digit = x % 10
    reversed_num  = reversed_num * 10 + digit
    x //=10
  return orginal == reversed_num