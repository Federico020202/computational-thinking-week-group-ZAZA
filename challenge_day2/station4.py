def solution_station_4(n):
    """Check if a number is prime."""
    if n <= 1:
        return False  # 0 and 1 are not prime numbers
    if n == 2:
        return True  # 2 is the only even prime number
    if n % 2 == 0:
        return False  # other even numbers are not prime
    
    # Check for factors from 3 to the square root of n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True

