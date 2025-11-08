data = [2, 4, 4, 4, 5, 5, 7, 9]

mean = sum(data) / len(data)
print("Mean : ", mean)

variance = sum((x - mean)**2 for x in data) / len(data)
print("Variance : ", variance)

# Standard deviation is just the square root of variance
import math

std_dev = math.sqrt(variance)
print("Standard Deviation:", std_dev)


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Mean and standard deviation
mu = mean
sigma = std_dev

# Generate values for x-axis
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 100)

# Compute the Gaussian (Normal) distribution
y = norm.pdf(x, mu, sigma)

# Plot the curve
plt.plot(x, y, color='blue')
plt.title('Gaussian (Normal) Distribution')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.grid(True)
plt.show()
