
import pandas as pd
def load_and_select_features(filepath, features):
  df = pd.read_csv(filepath)
  return df.loc[:, features]


def load_and_return_all_columns(file_path):
    df = pd.read_csv(file_path)
    return df

features=['age', 'class', 'flight_distance',
       'inflight_wifi_service', 'departure_arrival_time_convenient',
       'ease_of_online_booking', 'gate_location', 'food_and_drink',
       'online_boarding', 'seat_comfort', 'inflight_entertainment',
       'on_board_service', 'leg_room_service', 'baggage_handling',
       'checkin_service', 'inflight_service', 'cleanliness',
       'departure_delay_in_minutes', 'arrival_delay_in_minutes']
