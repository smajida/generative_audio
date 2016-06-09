
from __future__ import print_function
from lstm_utils import create_lstm_network
from audio_preprocessing.pipeline import load_matrix
from audio_preprocessing.cconfig import config

data = 'train_nonvib_flute'
folder_spec = 'D - data_flute_nonvib/'
# get trainings data
x_data, y_data = (folder_spec, data)

num_time_dimensions = x_data.shape[1]
num_frequency_dimensions = x_data.shape[2]
num_hidden_dimensions = 1024

batch_size=10
epochs = 40

model = create_lstm_network(num_time_dimensions, num_frequency_dimensions, num_hidden_dimensions)
print(model.summary())
print('Start Training')
model.fit(x_data, y_data, batch_size=batch_size, nb_epoch=epochs, verbose=1, validation_split=0.0)

print('Training complete')
model_output = config.datapath + data + '_weights'
model.save_weights(model_output)