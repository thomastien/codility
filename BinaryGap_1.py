def solution(N):
  # convert N to binary (just using bin(N) would make it start with "0b"))
  binary = "{0:b}".format(N)
  
  #So python split is not like PERL split, interestingly
  # e.g. 74 (1001010) will become [ '', '00', '0', '0']
  #     149 (10010101) will become [ '', '00', '0', '0', '']
  # So this is helpful in a sense, we'll always drop the last one in the array because it's either
  #   A) going to be a '', when legitimately bound by 1s
  #   B) not going to be a '', implying the last digit was a 0 so miss the qualifying condition anyway
  splitted = binary.split("1")
  
  # No matter what, the last element is either empty, or should be dropped (e.g. 100010, not encircled by 1s)
  splitted.pop()
  
  # Sort it so the longest binary gap is first
  splitted.sort(key=len, reverse=True)
  
  return len(splitted[0])
