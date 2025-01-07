import numpy as np

def calculate_lpf_coefficients(frequency, sample_rate, q_factor):
    w0 = 2 * np.pi * frequency / sample_rate
    
    alpha = np.sin(w0) / (2 * q_factor)
    
    cos_w0 = np.cos(w0)
    
    b0 = (1 - cos_w0) / 2
    b1 = 1 - cos_w0
    b2 = (1 - cos_w0) / 2
    a0 = 1 + alpha
    a1 = -2 * cos_w0
    a2 = 1 - alpha
    
    b0 /= a0
    b1 /= a0
    b2 /= a0
    a1 /= a0
    a2 /= a0
    
    return {
        "b0": b0,
        "b1": b1,
        "b2": b2,
        "a0": a0 / a0,
        "a1": a1,
        "a2": a2
    }

if __name__ == "__main__":
    cutoff_frequency = int(input("Cutoff frequency: "))
    sampling_rate = int(input("Sampling Rate: "))
    q_factor = float(input("Q Factor: "))
    
    coefficients = calculate_lpf_coefficients(cutoff_frequency, sampling_rate, q_factor)
    print("Low-Pass Filter Coefficients:")
    for coeff, value in coefficients.items():
        print(f"{coeff}: {value}")

