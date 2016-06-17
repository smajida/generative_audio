from train_func import train_func
from generate_seq import gen_seq_full
train = False
if train:
    train_dir = 'guitar_train'
    _, w_mat_name, d_mat_name = train_func(train_dir,
                                           n_hid_neurons=2048,
                                           n_rec_layers=1,
                                           epochs=100,
                                           highest_freq=1400,
                                           n_to_load=45,
                                           down_sampling=True,
                                           save_weights=True,
                                           chunks_per_sec=40,
                                           clip_len=5,
                                           add_spectra=True,
                                           activation='linear')

    folder_spec = '/instrument_samples/guitar_train/'
    data = d_mat_name
    model_name = w_mat_name
else:
    model_name = '/weight_matrices/piano_train_45files_5sec_40res_1400maxf_' + \
                 'spec_m1_2048hid_1lyrs_100ep_linearact'
    data = 'instrument_samples/piano_train/piano_train_45files_5sec_40res_1400maxf_spec'

folder_spec = '/instrument_samples/guitar_train/'

prime_length = 40
num_of_tests = 5
gen_seq_full(folder_spec=folder_spec, data=data, model_name=model_name,
             prime_length=prime_length, num_of_tests=num_of_tests)