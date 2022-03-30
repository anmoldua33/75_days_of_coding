def generate(self, numRows: int) -> List[List[int]]:
        retVal = [[1]]
        tmpVal = []
        
        for i in range(1, numRows):
            for j in range(i+1):
                # CHECK IF AT BOUNDS
                if j == 0 or j == i:
                    tmpVal.append(1)
                else:
                    # ADD VALUES FROM ROW ABOVE
                    value = retVal[i-1][j-1] + retVal[i-1][j]
                    tmpVal.append(value)
            # ADD COPY OF LIST TO RETURN LIST
            retVal.append(tmpVal.copy())
            tmpVal.clear()
        return retVal
