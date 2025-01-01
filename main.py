def to_mars_minutes(hour, minute):
    """Convert Mars time (hour and minute) into total Mars minutes."""
    return hour * 100 + minute


def overlap_in_minutes(D_start, D_end, P_start, P_end):
    """Figure out how many minutes the Deimos and Phobos intervals overlap."""

    # First, convert all times into Mars minutes (because it's easier to work with)
    D_start = to_mars_minutes(*D_start)
    D_end = to_mars_minutes(*D_end)
    P_start = to_mars_minutes(*P_start)
    P_end = to_mars_minutes(*P_end)

    # Twilight Rule: If the intervals just touch at one point, we count it as 1 minute
    if D_start == P_end or D_end == P_start:
        return 1

    # If the interval crosses midnight (wraps around), we adjust by adding 2500 minutes
    if D_start > D_end:  # Deimos wraps around midnight
        D_end += 2500
    if P_start > P_end:  # Phobos wraps around midnight as well
        P_end += 2500

    # Debugging: Print out adjusted intervals to see what's going on
    print(f"Adjusted Deimos: {D_start}-{D_end}")
    print(f"Adjusted Phobos: {P_start}-{P_end}")

    # Now check if there's an actual overlap
    if D_start <= P_end and P_start <= D_end:  # If they overlap at all
        # Find the overlap's start and end times
        overlap_start = max(D_start, P_start)
        overlap_end = min(D_end, P_end)

        print(f"Overlap start: {overlap_start}, overlap end: {overlap_end}")

        # Return the duration of the overlap in minutes (if it’s valid)
        return overlap_end - overlap_start if overlap_start < overlap_end else 0
    else:
        # If there’s no overlap, just return 0
        return 0
