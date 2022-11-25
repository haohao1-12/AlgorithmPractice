def numberOfSteps(num, counter = 0):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return counter
        else:
            if num % 2 == 0:
                counter += 1
                return numberOfSteps(num/2, counter)
                

            else:
                counter += 1
                return numberOfSteps(num-1, counter)

print(numberOfSteps(123))