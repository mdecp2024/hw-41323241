import math

def solve_motion(v0=None, v=None, a=None, d=None):
    """
    Solve for the missing variable in the motion equations given three known values.
    
    Parameters:
    v0 (float): Initial velocity (m/s) or None if not known.
    v (float): Final velocity (m/s) or None if not known.
    a (float): Acceleration (m/s²) or None if not known.
    d (float): Distance (m) or None if not known.
    
    Returns:
    float: The value of the missing variable.
    """
    # If initial velocity (v0) is missing
    if v0 is None:
        if v is not None and a is not None and d is not None:
            # Use equation: v0 = sqrt(v^2 - 2ad)
            return math.sqrt(v**2 - 2 * a * d)
        else:
            raise ValueError("Insufficient known values to solve for initial velocity.")
    
    # If final velocity (v) is missing
    elif v is None:
        if v0 is not None and a is not None and d is not None:
            # Use equation: v = sqrt(v0^2 + 2ad)
            return math.sqrt(v0**2 + 2 * a * d)
        else:
            raise ValueError("Insufficient known values to solve for final velocity.")
    
    # If acceleration (a) is missing
    elif a is None:
        if v0 is not None and v is not None and d is not None:
            # Use equation: a = (v^2 - v0^2) / (2 * d)
            return (v**2 - v0**2) / (2 * d)
        else:
            raise ValueError("Insufficient known values to solve for acceleration.")
    
    # If distance (d) is missing
    elif d is None:
        if v0 is not None and v is not None and a is not None:
            # Use equation: d = (v^2 - v0^2) / (2 * a)
            return (v**2 - v0**2) / (2 * a)
        else:
            raise ValueError("Insufficient known values to solve for distance.")
    
    # If all variables are given, return a message
    else:
        raise ValueError("Too many known values provided. Provide exactly three known values.")

# Example usage:
# 1. Solve for acceleration when v0=310 km/h, v=0, d=1000 m
v0_kmh = 310  # Initial velocity in km/h
v0 = (v0_kmh * 1000) / 3600  # Convert km/h to m/s
v = 0  # Final velocity (jet comes to a stop)
d = 1000  # Distance in meters

acceleration = solve_motion(v0=v0, v=v, d=d)
print(f"Required acceleration: {acceleration:.2f} m/s²")

# 2. Solve for final velocity when v0 = 20 m/s, a = 2 m/s², and d = 1000 m
v0 = 20  # m/s
a = 2  # m/s²
d = 1000  # meters

final_velocity = solve_motion(v0=v0, a=a, d=d)
print(f"Final velocity: {final_velocity:.2f} m/s")

# 3. Solve for distance when v0 = 10 m/s, v = 0 m/s, and a = -3 m/s² (deceleration)
v0 = 10  # m/s
v = 0  # m/s
a = -3  # m/s² (deceleration)

distance = solve_motion(v0=v0, v=v, a=a)
print(f"Stopping distance: {distance:.2f} meters")
