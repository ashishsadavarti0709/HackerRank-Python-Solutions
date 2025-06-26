# Name: Ashish Sadavarti
# Code: Torsional Angle Calculator
# Code Description: Implements a 3D Point class with vector operations (subtraction, dot product,
#                   cross product, absolute magnitude) to calculate the torsional angle
#                   between four input points.
# Copyright 2025

# This script defines a 'Points' class to represent 3D coordinates and perform
# common vector operations. It then uses these operations to calculate the
# torsional angle (also known as the dihedral angle) formed by four points
# (A, B, C, D). The torsional angle is the angle between two planes defined
# by (A, B, C) and (B, C, D).

import math # Import the math module for square root and arc cosine functions.

class Points(object):
    """
    Represents a 3D point (x, y, z) and supports vector operations.
    """
    def __init__(self, x, y, z):
        """
        Initializes a Points object with x, y, and z coordinates.
        """
        self.x = float(x) # Convert coordinates to float to ensure accurate calculations.
        self.y = float(y)
        self.z = float(z)

    def __sub__(self, other):
        """
        Overloads the subtraction operator (-) for Points objects.
        Returns a new Points object representing the vector from 'other' to 'self'.
        e.g., P1 - P2 represents the vector P2P1.
        """
        return Points(self.x - other.x, self.y - other.y, self.z - other.z)

    def dot(self, other):
        """
        Calculates the dot product of this point (vector) with another point (vector).
        The dot product of two vectors (x1, y1, z1) and (x2, y2, z2) is x1*x2 + y1*y2 + z1*z2.
        """
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        """
        Calculates the cross product of this point (vector) with another point (vector).
        The cross product of two vectors results in a new vector perpendicular to both.
        Its magnitude is related to the area of the parallelogram formed by the two vectors.
        """
        # (y1*z2 - z1*y2)
        cross_x = self.y * other.z - self.z * other.y
        # (z1*x2 - x1*z2)
        cross_y = self.z * other.x - self.x * other.z
        # (x1*y2 - y1*x2)
        cross_z = self.x * other.y - self.y * other.x
        return Points(cross_x, cross_y, cross_z)

    def absolute(self):
        """
        Calculates the magnitude (Euclidean length) of the vector from the origin to this point.
        For a vector (x, y, z), the magnitude is sqrt(x^2 + y^2 + z^2).
        """
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

if __name__ == '__main__':
    # This block handles input, performs the torsional angle calculation, and prints the result.
    # It expects four lines of input, each containing three space-separated float numbers
    # representing the (x, y, z) coordinates of points P1, P2, P3, and P4.

    try:
        # Define a list to store the four points.
        points = []
        point_names = ['P1', 'P2', 'P3', 'P4']

        # Read coordinates for four points.
        for i in range(4):
            # Prompt the user to enter coordinates for each point.
            coords_str = input(f"Enter space-separated X Y Z coordinates for point {point_names[i]} (e.g., '1.0 2.0 3.0'): ").split()
            # Convert string coordinates to floats and create a Points object.
            points.append(Points(*map(float, coords_str)))

        # Assign the Points objects to variables for clarity.
        A, B, C, D = points[0], points[1], points[2], points[3]

        # Calculate vectors AB, BC, and CD.
        # Vector AB = B - A
        AB = B - A
        # Vector BC = C - B
        BC = C - B
        # Vector CD = D - C
        CD = D - C

        # Calculate the normal vectors to the planes.
        # N1 is normal to the plane ABC (cross product of AB and BC)
        N1 = AB.cross(BC)
        # N2 is normal to the plane BCD (cross product of BC and CD)
        N2 = BC.cross(CD)

        # Calculate the dot product of N1 and N2.
        dot_product_N1_N2 = N1.dot(N2)

        # Calculate the magnitudes of N1 and N2.
        magnitude_N1 = N1.absolute()
        magnitude_N2 = N2.absolute()

        # Calculate the product of magnitudes.
        magnitudes_product = magnitude_N1 * magnitude_N2

        # Calculate the cosine of the angle.
        # Avoid division by zero if either magnitude is zero (e.g., if points are collinear).
        if magnitudes_product == 0:
            print("Error: Collinear points detected, cannot determine torsional angle.")
        else:
            cos_theta = dot_product_N1_N2 / magnitudes_product

            # Ensure cos_theta is within the valid range [-1, 1] for acos to prevent math domain error
            # Due to floating point inaccuracies, it might be slightly outside this range.
            cos_theta = max(-1.0, min(1.0, cos_theta))

            # Calculate the angle in radians using arc cosine.
            theta_radians = math.acos(cos_theta)

            # Determine the sign of the angle.
            # The sign of the torsional angle is determined by the scalar triple product (N1 x N2) . BC.
            # If positive, angle is positive; if negative, angle is negative.
            # This accounts for the handedness of the angle.
            cross_N1_N2 = N1.cross(N2)
            sign_determinant = cross_N1_N2.dot(BC)

            if sign_determinant < 0:
                theta_radians = -theta_radians

            # Convert the angle from radians to degrees and print the result, formatted to two decimal places.
            print(f"{math.degrees(theta_radians):.2f}")

    except ValueError:
        # Handles cases where input cannot be converted to float (e.g., non-numeric input).
        print("Invalid input. Please enter valid space-separated numbers for coordinates.")
    except IndexError:
        # Handles cases where fewer than 3 coordinates are provided per line.
        print("Input error: Please provide exactly three coordinates (X Y Z) for each point.")
    except Exception as e:
        # Catches any other unexpected errors during execution.
        print(f"An unexpected error occurred: {e}")

