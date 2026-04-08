import argparse
import os

def main():
    parser = argparse.ArgumentParser(description="Run the OpenEnv Client")
    parser.add_argument("--scenario", type=str, default="user", help="Scenario to run")
    args = parser.parse_args()

    print(f"Initializing Actuarial Risk Environment Client for scenario: {args.scenario}...")
    print("Agent is ready to receive pricing strategies.")

if __name__ == "__main__":
    main()
