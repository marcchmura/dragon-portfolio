import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_excel("data.xlsx")
print(df.head())

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
    # Calculate portfolio return for each month
    df['Portfolio_Return'] = (df['^SP500TR'] * weights['^SP500TR'] +
                              df['TRSY.MI'] * weights['TRSY.MI'] +
                              df['GC=F'] * weights['GC=F'] +
                              df['COMMO'] * weights['COMMO'] +
                              df['LONGVOL'] * weights['LONGVOL'])

    # Initialize the portfolio with $1
    initial_investment = 1
    df['Portfolio_Value'] = initial_investment * (1 + df['Portfolio_Return']).cumprod()

    # Plot the portfolio value evolution
    plt.plot(df['Date'], df['Portfolio_Value'], label=f'{portfolio_name} Portfolio')

# Customize the plot
plt.title('MODERN PORTFOLIO IMPLEMENTATION')
plt.ylabel('GROWTH OF $1')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
