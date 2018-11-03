# import modules
import functions.f_movement as f_move
import functions.f_load_data as f_load
import os
import pickle

# obtain the names, csv_files, path, start_dt, end_dt
names = f_load.names
csv_files = f_load.csv_files
path = f_load.path
start_dt = f_load.start_dt
end_dt = f_load.end_dt

# calculate movement
move = f_move.predict_movement(csv_files, names, path, start_dt, end_dt)
move.get_movements()

# get the movement dataframe
move.periods_of_volatility()
movement = move.dataframe
print(movement)

# save the volatility_dataframe into pickle
file_path = os.path.dirname(os.path.realpath(__file__))
save_path = file_path + '/docs/' + 'movement.pickle'
with open(save_path, 'wb') as f:
    pickle.dump(movement, f)
