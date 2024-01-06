batch_size   = 10

config = {}
# set the parameters related to the training and testing set
data_train_opt = {} 
data_train_opt['batch_size'] = batch_size
data_train_opt['grayscale'] = True
data_train_opt['unsupervised'] = False
data_train_opt['epoch_size'] = None
data_train_opt['random_sized_crop'] = False
data_train_opt['dataset_name'] = 'mnist'
data_train_opt['dataset_len'] = 100
data_train_opt['split'] = 'train'

data_test_opt = {}
data_test_opt['batch_size'] = batch_size
data_test_opt['grayscale'] = True
data_test_opt['unsupervised'] = False
data_test_opt['epoch_size'] = None
data_test_opt['random_sized_crop'] = False
data_test_opt['dataset_name'] = 'mnist'
data_test_opt['split'] = 'test'

config['data_train_opt'] = data_train_opt
config['data_test_opt']  = data_test_opt
config['max_num_epochs'] = 50

networks = {}
feat_net_opt = {'num_classes': 2, 'num_inchannels': 1, 'num_stages': 4, 'use_avg_on_conv3': False}
feat_pretrained_file = './experiments/MNIST_Base_Model_2Rot_4Block/model_net_epoch10'
networks['feat_extractor'] = {'def_file': 'architectures/NetworkInNetwork.py', 'pretrained': feat_pretrained_file, 'opt': feat_net_opt,  'optim_params': None} 

cls_net_optim_params = {'optim_type': 'sgd', 'lr': 0.1, 'momentum':0.9, 'weight_decay': 5e-4, 'nesterov': True, 'LUT_lr':[(35, 0.1),(70, 0.02),(85, 0.004),(100, 0.0008)]}
cls_net_opt = {'num_classes':10, 'nChannels':192, 'cls_type':'NIN_ConvBlock3_grayscale'}
networks['classifier'] = {'def_file': 'architectures/NonLinearClassifier.py', 'pretrained': None, 'opt': cls_net_opt, 'optim_params': cls_net_optim_params}
config['out_feat_keys'] = ['conv2']

config['networks'] = networks

criterions = {}
criterions['loss'] = {'ctype':'CrossEntropyLoss', 'opt':None}
config['criterions'] = criterions
config['algorithm_type'] = 'FeatureClassificationModel'
config['best_metric'] = 'prec1'
