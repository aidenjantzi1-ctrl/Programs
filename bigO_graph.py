import matplotlib.pyplot as plt
import numpy as np
import math

# 1. Define high-resolution input sizes (n) up to 1000
n = np.linspace(1.5, 50, 5000)
alpha_n = np.full_like(n, 1.5) + (n / 2000.0) 

# 2. Complete Big O Dictionary (Configured safely to avoid warnings/overflows)
functions = {
    "$O(1)$": np.ones_like(n),
    "$O(\\alpha(n))$": alpha_n,
    "$O(\\log \\log n)$": np.log2(np.log2(n)),
    "$O(\\log n)$": np.log2(n),
    "$O(\\sqrt{n})$": np.sqrt(n),
    "$O(n)$": n,
    "$O(n \\log \\log n)$": n * np.log2(np.log2(n)),
    "$O(n \\log n)$": n * np.log2(n),
    "$O(n^2)$": n ** 2,
    "$O(n^3)$": n ** 3,
    "$O(2^n)$": np.array([2 ** x if x < 30 else 1e9 for x in n]),
    "$O(n!)$": np.array([math.factorial(int(x)) if x < 13 else np.inf for x in n]),
    "$O(n^n)$": np.array([x ** x if x < 10 else 1e9 for x in n])
}

# 3. Setup window dimensions (Clean 1:1 Square Aspect Ratio)
plt.figure(figsize=(9, 9), dpi=100)
plt.title("Big O Notation Complexity Chart", fontsize=14, fontweight='bold', pad=40)
plt.xlabel("Elements / Input Size (n)", fontsize=11, labelpad=12)
plt.ylabel("Operations / Time Spent (Log Scale)", fontsize=11, labelpad=12)

ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_box_aspect(1)

# Chart boundaries and logarithmic scale configuration
X_MAX = 50
Y_MAX = 1000000
Y_MIN = 0.5 

plt.xlim(1.5, X_MAX)
plt.ylim(Y_MIN, Y_MAX)
plt.yscale('log')

# 4. First pass: Plot lines and gather single-value intersection floats
label_positions = []

for label, y_values in functions.items():
    plt.plot(n, y_values, color="#222222", lw=1.5)
    
    # Track where the curve intersects either the top or right boundary
    # Flattening using [0] to extract a pure 1D array of indices immediately
    valid_indices = np.where((y_values <= Y_MAX) & (n <= X_MAX))[0]
    
    if valid_indices.size > 0:
        last_idx = int(valid_indices[-1])
        intersect_x = float(n[last_idx])
        intersect_y = float(y_values[last_idx])
        label_positions.append([intersect_x, intersect_y, label])

# 5. Spacing pass: Sort and isolate overlapping label targets
# Uses a lambda sorting key to specifically evaluate only the Y float coordinate
label_positions.sort(key=lambda item: item[1]) 
MIN_LOG_DISTANCE = 0.22 

for i in range(1, len(label_positions)):
    prev_log_y = math.log10(label_positions[i-1][1])
    curr_log_y = math.log10(label_positions[i][1])
    
    if (curr_log_y - prev_log_y) < MIN_LOG_DISTANCE:
        adjusted_y = 10 ** (prev_log_y + MIN_LOG_DISTANCE)
        label_positions[i][1] = adjusted_y

# 6. Second pass: Place perfectly spaced text anchors onto boundaries
for intersect_x, final_y, label in label_positions:
    raw_y = Y_MAX
    raw_x = X_MAX
    for orig_label, orig_y_values in functions.items():
        if orig_label == label:
            valid_indices = np.where((orig_y_values <= Y_MAX) & (n <= X_MAX))[0]
            if valid_indices.size > 0:
                last_idx = int(valid_indices[-1])
                raw_y = float(orig_y_values[last_idx])
                raw_x = float(n[last_idx])
            break

    # Connect shifted labels with a subtle dotted indicator line
    has_arrow = abs(math.log10(final_y) - math.log10(raw_y)) > 0.02
    x_offset = X_MAX * 0.03 if raw_x == X_MAX else X_MAX * 0.01
    
    ax.annotate(
        label, 
        xy=(raw_x, raw_y),                     
        xytext=(raw_x + x_offset, final_y),
        va="center",                        
        ha="left",                          
        fontsize=10, 
        fontweight="bold",
        arrowprops=dict(arrowstyle="-", color="#777777", lw=0.8, ls=":") if has_arrow else None
    )

# 7. Final grid layout adjustments
plt.grid(True, which="both", linestyle=":", alpha=0.4, color="gray")
plt.subplots_adjust(right=0.78) 
plt.tight_layout()

# 8. Open the interactive window exclusively
plt.show()
