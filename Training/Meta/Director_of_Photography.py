'''
A photography set consists of
N
N cells in a row, numbered from
1
1 to
N
N in order, and can be represented by a string
C
C of length
N
N. Each cell
i
i is one of the following types (indicated by
C
i
C
i
​
 , the
i
ith character of
C
C):
If
C
i
C
i
​
  = “P”, it is allowed to contain a photographer
If
C
i
C
i
​
  = “A”, it is allowed to contain an actor
If
C
i
C
i
​
  = “B”, it is allowed to contain a backdrop
If
C
i
C
i
​
  = “.”, it must be left empty
A photograph consists of a photographer, an actor, and a backdrop, such that each of them is placed in a valid cell, and such that the actor is between the photographer and the backdrop. Such a photograph is considered artistic if the distance between the photographer and the actor is between
X
X and
Y
Y cells (inclusive), and the distance between the actor and the backdrop is also between
X
X and
Y
Y cells (inclusive). The distance between cells
i
i and
j
j is
∣
i
−
j
∣
∣i−j∣ (the absolute value of the difference between their indices).
Determine the number of different artistic photographs which could potentially be taken at the set. Two photographs are considered different if they involve a different photographer cell, actor cell, and/or backdrop cell.
Constraints
1
≤
N
≤
200
1≤N≤200
1
≤
X
≤
Y
≤
N
1≤X≤Y≤N
Sample test case #1
N = 5
C = APABA
X = 1
Y = 2
Expected Return Value = 1
Sample test case #2
N = 5
C = APABA
X = 2
Y = 3
Expected Return Value = 0
Sample test case #3
N = 8
C = .PBAAP.B
X = 1
Y = 3
Expected Return Value = 3
Sample Explanation
In the first case, the absolute distances between photographer/actor and actor/backdrop must be between
1
1 and
2
2. The only possible photograph that can be taken is with the
3
3 middle cells, and it happens to be artistic.
In the second case, the only possible photograph is again taken with the
3
3 middle cells. However, as the distance requirement is between
2
2 and
3
3, it is not possible to take an artistic photograph.
In the third case, there are
4
4 possible photographs, illustrated as follows:
.P.A...B
.P..A..B
..BA.P..
..B.AP..
All are artistic except the first, where the actor and backdrop exceed the maximum distance of
3
3.



'''

def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    # Write your code here
    count = 0

    for i in range(N):
        if C[i] == 'A':  # Actor's position
            for j in range(max(0, i - Y), min(N, i - X + 1)):  # Photographer's possible positions
                if C[j] == 'P':
                    for k in range(max(i + X, j + X), min(N, i + Y + 1)):  # Backdrop's possible positions
                        if C[k] == 'B':
                            count += 1

            for j in range(i + X, min(N, i + Y + 1)):  # Photographer's possible positions (opposite order)
                if C[j] == 'P':
                    for k in range(max(0, i - Y), min(i - X + 1, j - X)):  # Backdrop's possible positions
                        if C[k] == 'B':
                            count += 1

    return count


print(getArtisticPhotographCount(5,"APABA",1,2))
print(getArtisticPhotographCount(8," PBAAP B",1,3))
