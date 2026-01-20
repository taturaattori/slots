from machine import Machine

def run_monte_carlo_simulation(num_spins=100000, bet_size=1.00, num_runs=1):
    """
    Run Monte Carlo simulation to test RTP
    
    Args:
        num_spins: Number of spins per simulation run
        bet_size: Bet amount per spin
        num_runs: Number of simulation runs to average
    """
    print(f"\n{'='*60}")
    print(f"Monte Carlo Simulation - Testing RTP")
    print(f"{'='*60}")
    print(f"Spins per run: {num_spins:,}")
    print(f"Bet size: ${bet_size:.2f}")
    print(f"Number of runs: {num_runs}")
    print(f"{'='*60}\n")
    
    all_rtps = []
    all_hit_rates = []
    
    for run in range(num_runs):
        slot_machine = Machine()
        result = slot_machine.simulation(spins=num_spins, bet_size=bet_size)
        
        rtp_value = float(result['RTP'].rstrip('%'))
        hit_rate_value = float(result['hit_rate'].rstrip('%'))
        all_rtps.append(rtp_value)
        all_hit_rates.append(hit_rate_value)
        
        if num_runs == 1:
            print(f"Results:")
            print(f"  Total Spins: {result['total_spins']:,}")
            print(f"  Winning Spins: {result['winning_spins']:,}")
            print(f"  Hit Rate: {result['hit_rate']}")
            print(f"  Total Wagered: ${result['total_wagered']}")
            print(f"  Total Won: ${result['total_won']}")
            print(f"  Final Balance: ${result['final_balance']}")
            print(f"  RTP: {result['RTP']}")
            print(f"\nWin Frequency by Symbol:")
            for symbol_combo, count in sorted(result['win_frequency'].items(), key=lambda x: x[1], reverse=True):
                symbol, match_count = symbol_combo.rsplit('_', 1)
                print(f"    {symbol} x{match_count}: {count:,} times")
        else:
            print(f"Run {run + 1}/{num_runs}: RTP = {rtp_value:.2f}%, Hit Rate = {hit_rate_value:.2f}%")
    
    if num_runs > 1:
        avg_rtp = sum(all_rtps) / len(all_rtps)
        avg_hit_rate = sum(all_hit_rates) / len(all_hit_rates)
        min_rtp = min(all_rtps)
        max_rtp = max(all_rtps)
        
        print(f"\n{'='*60}")
        print(f"Average Results Across {num_runs} Runs:")
        print(f"{'='*60}")
        print(f"  Average RTP: {avg_rtp:.2f}%")
        print(f"  RTP Range: {min_rtp:.2f}% - {max_rtp:.2f}%")
        print(f"  Average Hit Rate: {avg_hit_rate:.2f}%")
        print(f"{'='*60}\n")

if __name__ == "__main__":
    # Run a single simulation with 100,000 spins
    run_monte_carlo_simulation(num_spins=1000000, bet_size=1.00, num_runs=1)
    
    # Uncomment to run multiple simulations for more accurate RTP calculation
    # run_monte_carlo_simulation(num_spins=100000, bet_size=1.00, num_runs=10)