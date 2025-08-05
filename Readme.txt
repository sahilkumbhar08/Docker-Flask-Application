Blockhouse Quantitative Developer Work Trial - MBP-10 Reconstruction

Overview
--------
This project implements an efficient MBP-10 order book reconstruction from MBO data using C++. The code processes a stream of market actions (A, M, T, F, C, R) and generates a market-by-price order book with up to 10 levels for both bid and ask sides, adhering to the specified requirements.

Optimization Strategies
----------------------
1. **Data Structures**:
   - Used `std::map` for bids and asks with appropriate ordering (`std::greater` for bids, default for asks) to maintain sorted price levels efficiently.
   - Employed a `std::vector` for pending trades to handle the T -> F -> C sequence, allowing O(n) lookup for matching trades.
   - Considered `std::unordered_map` for O(1) lookups but chose `std::map` for automatic sorting and simpler level management.

2. **Memory Efficiency**:
   - Minimized memory usage by storing only necessary data (price, size, side) in the Order struct.
   - Cleared zero-size levels immediately to reduce memory footprint.
   - Avoided redundant data copies during processing.

3. **Performance Optimizations**:
   - Used `-O3` optimization flag in the Makefile for maximum compiler optimizations.
   - Processed input stream sequentially to leverage cache locality.
   - Minimized string operations by parsing CSV fields directly into required types.
   - Output MBP-10 data incrementally to avoid buffering entire output.

4. **Special Handling**:
   - Ignored the initial "clear[R]" action by skipping the first row and clearing the book.
   - Handled T -> F -> C sequences by storing trades temporarily and applying changes to the opposite side of the book when a matching cancel (C) is found.
   - Ignored trades with side 'N' as specified.

5. **Output Formatting**:
   - Ensured output matches mbp.csv format with 10 levels per side, padding with zeros if fewer levels exist.
   - Used `std::fixed` and `std::setprecision(2)` for consistent price formatting.

Running the Code
----------------
1. **Prerequisites**:
   - A C++17 compatible compiler (e.g., g++).
   - Input file `mbo.csv` in the same directory.

2. **Build**:
   ```bash
   make
   ```

3. **Run**:
   ```bash
   ./reconstruction_blockhouse mbo.csv
   ```

4. **Output**:
   - Generates `mbp_output.csv` with the MBP-10 data in the format: `ts,bid_price_0,bid_size_0,...,bid_price_9,bid_size_9,ask_price_0,ask_size_0,...,ask_price_9,ask_size_9`.

Notes and Limitations
--------------------
- **Trade Matching**: The current implementation assumes T, F, and C actions for a trade occur in sequence and have exact price and size matches. In a production environment, additional validation (e.g., order IDs) could improve robustness.
- **Performance Trade-offs**: Using `std::map` provides O(log n) operations but ensures sorted levels. For ultra-high-frequency data, a custom data structure (e.g., a fixed-size array for 10 levels) could further improve performance at the cost of flexibility.
- **Error Handling**: Basic file I/O error checking is included. Additional checks (e.g., for malformed CSV) could be added for robustness.
- **Unit Tests**: Not included due to time constraints, but a test suite could validate edge cases (e.g., empty books, large trades, rapid updates).

Potential Improvements
---------------------
- **Custom Data Structure**: Implement a fixed-size priority queue or array for the top 10 levels to reduce overhead.
- **Parallel Processing**: For very large datasets, consider batch processing or parallel I/O.
- **Profiling**: Use tools like `perf` or `valgrind` to identify bottlenecks specific to the input data.

This implementation balances correctness, performance, and code clarity, with a focus on meeting the MBP-10 output requirements efficiently.