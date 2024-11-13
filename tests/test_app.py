import pytest
import os
import tempfile
import pandas as pd

@pytest.fixture(scope="session")
def test_env():
    """Setup test environment variables"""
    os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
    return os.environ

@pytest.fixture(scope="session")
def test_files():
    """Create test CSV files"""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create flight bookings test data
        flight_df = pd.DataFrame({
            'booking_id': range(1, 6),
            'flight_id': ['F1', 'F2', 'F3', 'F4', 'F5'],
            'passenger_name': ['John Doe', 'Jane Smith', None, 'Bob Wilson', 'Alice Brown'],
            'seat_number': ['1A', '2B', '3C', None, '5E'],
            'price': [100.0, 200.0, None, 400.0, 500.0]
        })
        flight_path = os.path.join(tmpdir, 'flight_bookings_test.csv')
        flight_df.to_csv(flight_path, index=False)
        
        # Create airline reference test data
        airline_df = pd.DataFrame({
            'airline_id': ['A1', 'A2', 'A3'],
            'airline_name': ['Air One', 'Sky Jets', 'Blue Wings']
        })
        airline_path = os.path.join(tmpdir, 'airline_reference_test.csv')
        airline_df.to_csv(airline_path, index=False)
        
        yield {
            'flight_bookings': flight_path,
            'airline_reference': airline_path
        }