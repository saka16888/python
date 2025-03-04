def maxAdditionalDiners(N, K, M, S):
    # Sort the occupied seats
    S.sort()

    additional_diners = 0
    prev_end = 0  # Tracks the end of the last occupied region

    # Check empty spaces before the first diner
    if S[0] > 1:
        gap = S[0] - 1  # Space before first occupied seat
        additional_diners += gap // (K + 1)

    # Check spaces between occupied seats
    for i in range(M):
        if i == 0:
            prev_end = S[i]  # Initialize prev_end
            continue

        gap = S[i] - prev_end - 1  # Space between two occupied seats
        if gap > 2 * K:  # If enough space exists for at least one diner
            additional_diners += (gap - K) // (K + 1)

        prev_end = S[i]  # Update prev_end to current seat

    # Check empty spaces after the last diner
    if S[-1] < N:
        gap = N - S[-1]  # Space after last occupied seat
        additional_diners += gap // (K + 1)

    return additional_diners


N = 10; K = 1; M = 2; S = [2, 6]
print(maxAdditionalDiners(N, K, M, S))
# expected 3

N = 15; K = 2; M = 3; S = [11, 6, 14]
print(maxAdditionalDiners(N, K, M, S))
# expected 1