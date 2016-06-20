from train_func import train_func
from generate_seq import gen_seq_full

train = True
if train:
    train_dir = 'guitar_train'
    _, w_mat_name, d_mat_name = train_func(train_dir,
                                           n_hid_neurons=512,
                                           n_rec_layers=2,
                                           epochs=100,
                                           highest_freq=1400,
                                           n_to_load=5,
                                           down_sampling=True,
                                           save_weights=True,
                                           chunks_per_sec=40,
                                           clip_len=5,
                                           add_spectra=False,
                                           architecture='1',
                                           mean_std_per_file=True,
                                           activation='linear')

    folder_spec = '/instrument_samples/guitar_train/'
    data = d_mat_name
    model_name = w_mat_name
else:
    model_name = 'guitar_train_45files_5sec_40res_1400maxf_spec_m1_2048hid_1lyrs_100ep_linearact'
    data = 'guitar_train_45files_5sec_40res_1400maxf_spec'

folder_spec = '/instrument_samples/guitar_train/'

prime_length = 40
num_of_tests = 3
gen_seq_full(folder_spec=folder_spec, data=data, model_name=model_name,
             prime_length=prime_length, num_of_tests=num_of_tests, add_spectra=True, mean_std_per_file=True)