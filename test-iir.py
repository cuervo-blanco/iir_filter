import numpy as np
from calculate_lpf_coefficients import calculate_lpf_coefficients
from iir_filter import IIRFilter

def test_lpf():
    cutoff_frequency = 500
    sampling_rate = 2000
    q_factor = 0.707

    coefficients = calculate_lpf_coefficients(cutoff_frequency, sampling_rate, q_factor)
    print("Filter Coefficients:", coefficients)

    iir_filter = IIRFilter(
        b_0=coefficients["b0"],
        b_1=coefficients["b1"],
        b_2=coefficients["b2"],
        a_1=coefficients["a1"],
        a_2=coefficients["a2"]
    )

    t = np.linspace(0, 1, sampling_rate, endpoint=False)
    low_freq_signal = np.sin(2 * np.pi * 100 * t)
    high_freq_signal = np.sin(2 * np.pi * 1000 * t)
    input_signal = low_freq_signal + high_freq_signal

    output_signal = np.zeros_like(input_signal)
    iir_filter.filter(input_signal, output_signal)

    print("Input Signal (first 10 samples):", input_signal[:10])
    print("Output Signal (first 10 samples):", output_signal[:10])

    low_passed = np.abs(np.fft.rfft(output_signal))
    freqs = np.fft.rfftfreq(len(output_signal), 1 / sampling_rate)

    low_band_energy = np.sum(low_passed[(freqs >= 90) & (freqs <= 110)])
    high_band_energy = np.sum(low_passed[(freqs >= 900) & (freqs <= 1100)])

    assert low_band_energy > high_band_energy, "Filter did not attenuate high frequencies sufficiently."
    print("Test passed: Low frequencies are preserved, high frequencies are attenuated.")

if __name__ == "__main__":
    test_lpf()

