import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_excel("data.xlsx")
print(df.head())

# Leverage multipliers to reach 8% volatility
leverage_factors = {
    'Dragon': 1.38408304,
    '40/60': 1.08991826,
    'Dragon w/o Commo': 1.09439124,
    'Dragon w/o Gold': 1.34907251
}

# Define portfolio allocations
portfolios = {
    'Dragon': {
        '^SP500TR': 0.24,
        'TRSY.MI': 0.18,
        'GC=F': 0.19,
        'COMMO': 0.21,
        'LONGVOL': 0.18
    },
    '40/60': {
        '^SP500TR': 0.40,
        'TRSY.MI': 0.60,
        'GC=F': 0.0,
        'COMMO': 0.0,
        'LONGVOL': 0.0
    },
    'Dragon w/o Commo': {
        '^SP500TR': 0.40,
        'TRSY.MI': 0.30,
        'GC=F': 0.0,
        'COMMO': 0.0,
        'LONGVOL': 0.30
    },
    'Dragon w/o Gold': {
        '^SP500TR': 0.30,
        'TRSY.MI': 0.22,
        'GC=F': 0.0,
        'COMMO': 0.26,
        'LONGVOL': 0.22
    }
}

# Initialize figure for plotting
plt.figure(figsize=(10, 6))

# Run simulations for each portfolio
for portfolio_name, weights in portfolios.items():
    # Calculate monthly return
    df['Portfolio_Return'] = (
        df['^SP500TR'] * weights.get('^SP500TR', 0) +
        df['TRSY.MI'] * weights.get('TRSY.MI', 0) +
        df['GC=F'] * weights.get('GC=F', 0) +
        df['COMMO'] * weights.get('COMMO', 0) +
        df['LONGVOL'] * weights.get('LONGVOL', 0)
    )

    # Apply leverage to match 8% volatility
    leverage = leverage_factors.get(portfolio_name, 1.0)
    df['Leveraged_Return'] = df['Portfolio_Return'] * leverage

    # Calculate cumulative growth of $1
    df['Portfolio_Value'] = (1 + df['Leveraged_Return']).cumprod()

    # Plot the growth
    plt.plot(df['Date'], df['Portfolio_Value'], label=portfolio_name)

# Customize the plot
plt.title('MODERN PORTFOLIO IMPLEMENTATION')
plt.ylabel('GROWTH OF $1 AT 8% VOLATILITY')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
