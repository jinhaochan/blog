Title: Microsoft Kaggle Competition
Date: 2019-03-31 09:38
Author: jinhaochan
Category: Data Science
Tags: Kaggle
Slug: microsoft-kaggle-competition
Status: published

<!-- wp:paragraph -->

This is the write up for my solution for the Microsoft Malware Prediction

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

<https://www.kaggle.com/c/microsoft-malware-prediction>

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

I got pretty high up the leader board, but it was nothing that I was proud of, because:

<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->

1.  I grossly overfitted my model
2.  The final result was a blend of another kernel
3.  All my attempts at feature engineering failed

<!-- /wp:list -->

<!-- wp:paragraph -->

And I'm now officially ceasing efforts to improve my score, because:

<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->

1.  I'm not learning anything new, just mindlessly tweaking hyperparameters and hoping one of them works
2.  I don't think I've got the basics down yet, and this challenge was way over my head. I feel I should start with something simpler
3.  And most importantly, I'm no longer having fun

<!-- /wp:list -->

<!-- wp:paragraph -->

But wait! Doing such a hard competition really taught me many concepts, such as:

<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->

1.  Adversarial Cross Validation
2.  How to properly use LightGBM
3.  The real problem of overfitting, which LightGBM does really fast
4.  Blending and Ensembling is a powerful method for getting good results

<!-- /wp:list -->

<!-- wp:paragraph -->

Below shows one of the code variants I've used. They were all mostly the same, with a few hyperparameters being different, and some failed attempts at feature engineering.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

The most important features were Version numbers, and there's probably some way to exploit that.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

My single model (which I believe grossly overfitted, because I set `num_leaves=8000` got me a score of 0.684. I blended with another blended kernel of 0.688, and my final score was 0.692.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

I think this got me off at the wrong start because I was working and tweaking with those overfitted hyperparameters, when they were wrong in the first place.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Anyway, on to the next competition!  

<!-- /wp:paragraph -->

<!-- wp:code -->

``` {.wp-block-code}
# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import pandas as pd
import numpy as np
import gc
import matplotlib as mpl
import matplotlib.pyplot as plt
import warnings

import lightgbm as lgb
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import StratifiedKFold
from sklearn import preprocessing
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

import category_encoders as ce

le = preprocessing.LabelEncoder()


# Any results you write to the current directory are saved as output.

dtypes = {
        #'MachineIdentifier':                                    'category',
        'ProductName':                                          'category',
        'EngineVersion':                                        'category',
        'AppVersion':                                           'category',
        'AvSigVersion':                                         'category',
        'IsBeta':                                               'int8',
        'RtpStateBitfield':                                     'float16',
        'IsSxsPassiveMode':                                     'int8',
        'DefaultBrowsersIdentifier':                            'float16',
        'AVProductStatesIdentifier':                            'float32',
        'AVProductsInstalled':                                  'float16',
        'AVProductsEnabled':                                    'float16',
        'HasTpm':                                               'int8',
        'CountryIdentifier':                                    'int32',
        'CityIdentifier':                                       'float32',
        'OrganizationIdentifier':                               'float16',
        'GeoNameIdentifier':                                    'float32',
        'LocaleEnglishNameIdentifier':                          'int32',
        'Platform':                                             'category',
        'Processor':                                            'category',
        'OsVer':                                                'category',
        'OsBuild':                                              'int16',
        'OsSuite':                                              'int16',
        'OsPlatformSubRelease':                                 'category',
        'OsBuildLab':                                           'category',
        'SkuEdition':                                           'category',
        'IsProtected':                                          'float16',
        'AutoSampleOptIn':                                      'int8',
        'PuaMode':                                              'category',
        'SMode':                                                'float16',
        'IeVerIdentifier':                                      'float32',
        'SmartScreen':                                          'category',
        'Firewall':                                             'float16',
        'UacLuaenable':                                         'float64',
        'Census_MDC2FormFactor':                                'category',
        'Census_DeviceFamily':                                  'category',
        'Census_OEMNameIdentifier':                             'float32',
        'Census_OEMModelIdentifier':                            'float32',
        'Census_ProcessorCoreCount':                            'float16',
        'Census_ProcessorManufacturerIdentifier':               'float16',
        'Census_ProcessorModelIdentifier':                      'float32',
        'Census_ProcessorClass':                                'category',
        'Census_PrimaryDiskTotalCapacity':                      'float32',
        'Census_PrimaryDiskTypeName':                           'category',
        'Census_SystemVolumeTotalCapacity':                     'float32',
        'Census_HasOpticalDiskDrive':                           'int8',
        'Census_TotalPhysicalRAM':                              'float32',
        'Census_ChassisTypeName':                               'category',
        'Census_InternalPrimaryDiagonalDisplaySizeInInches':    'float32',
        'Census_InternalPrimaryDisplayResolutionHorizontal':    'float32',
        'Census_InternalPrimaryDisplayResolutionVertical':      'float32',
        'Census_PowerPlatformRoleName':                         'category',
        'Census_InternalBatteryType':                           'category',
        'Census_InternalBatteryNumberOfCharges':                'float32',
        'Census_OSVersion':                                     'category',
        'Census_OSArchitecture':                                'category',
        'Census_OSBranch':                                      'category',
        'Census_OSBuildNumber':                                 'int32',
        'Census_OSBuildRevision':                               'int32',
        'Census_OSEdition':                                     'category',
        'Census_OSSkuName':                                     'category',
        'Census_OSInstallTypeName':                             'category',
        'Census_OSInstallLanguageIdentifier':                   'float16',
        'Census_OSUILocaleIdentifier':                          'int32',
        'Census_OSWUAutoUpdateOptionsName':                     'category',
        'Census_IsPortableOperatingSystem':                     'int8',
        'Census_GenuineStateName':                              'category',
        'Census_ActivationChannel':                             'category',
        'Census_IsFlightingInternal':                           'float16',
        'Census_IsFlightsDisabled':                             'float16',
        'Census_FlightRing':                                    'category',
        'Census_ThresholdOptIn':                                'float16',
        'Census_FirmwareManufacturerIdentifier':                'float32',
        'Census_FirmwareVersionIdentifier':                     'float32',
        'Census_IsSecureBootEnabled':                           'int8',
        'Census_IsWIMBootEnabled':                              'float16',
        'Census_IsVirtualDevice':                               'float16',
        'Census_IsTouchEnabled':                                'int8',
        'Census_IsPenCapable':                                  'int8',
        'Census_IsAlwaysOnAlwaysConnectedCapable':              'float16',
        'Wdft_IsGamer':                                         'float16',
        'Wdft_RegionIdentifier':                                'float32',
        'HasDetections':                                        'int8'
    }


# read data
print("Reading Data")
df_train = pd.read_csv('sorted.csv', nrows=5000000, dtype=dtypes).set_index('MachineIdentifier')
df_test = pd.read_csv('test.csv', dtype=dtypes).set_index('MachineIdentifier')
```

<!-- /wp:code -->

<!-- wp:code -->

``` {.wp-block-code}
Reading Data
```

<!-- /wp:code -->

<!-- wp:code -->

``` {.wp-block-code}
len(df_train)

features = [f for f in df_train.columns if f != 'HasDetections']

#assign target variable to y_train
y = df_train['HasDetections']
Train = df_train[features]
Test = df_test[features]
```

<!-- /wp:code -->

<!-- wp:heading -->

Feature Engineering
-------------------

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:code -->

``` {.wp-block-code}
def add_noise(series, noise_level):
    return series * (1 + noise_level * np.random.randn(len(series)))

def target_encode(trn_series=None, 
                  tst_series=None, 
                  target=None, 
                  min_samples_leaf=1, 
                  smoothing=1,
                  noise_level=0):
    """
    Smoothing is computed like in the following paper by Daniele Micci-Barreca
    https://kaggle2.blob.core.windows.net/forum-message-attachments/225952/7441/high%20cardinality%20categoricals.pdf
    trn_series : training categorical feature as a pd.Series
    tst_series : test categorical feature as a pd.Series
    target : target data as a pd.Series
    min_samples_leaf (int) : minimum samples to take category average into account
    smoothing (int) : smoothing effect to balance categorical average vs prior  
    """ 
    assert len(trn_series) == len(target)
    assert trn_series.name == tst_series.name
    temp = pd.concat([trn_series, target], axis=1)
    # Compute target mean 
    averages = temp.groupby(by=trn_series.name)[target.name].agg(["mean", "count"])
    # Compute smoothing
    smoothing = 1 / (1 + np.exp(-(averages["count"] - min_samples_leaf) / smoothing))
    # Apply average function to all target data
    prior = target.mean()
    # The bigger the count the less full_avg is taken into account
    averages[target.name] = prior * (1 - smoothing) + averages["mean"] * smoothing
    averages.drop(["mean", "count"], axis=1, inplace=True)
    # Apply averages to trn and tst series
    ft_trn_series = pd.merge(
        trn_series.to_frame(trn_series.name),
        averages.reset_index().rename(columns={'index': target.name, target.name: 'average'}),
        on=trn_series.name,
        how='left')['average'].rename(trn_series.name + '_mean').fillna(prior)
    # pd.merge does not keep the index so restore it
    ft_trn_series.index = trn_series.index 
    ft_tst_series = pd.merge(
        tst_series.to_frame(tst_series.name),
        averages.reset_index().rename(columns={'index': target.name, target.name: 'average'}),
        on=tst_series.name,
        how='left')['average'].rename(trn_series.name + '_mean').fillna(prior)
    # pd.merge does not keep the index so restore it
    ft_tst_series.index = tst_series.index
    return add_noise(ft_trn_series, noise_level), add_noise(ft_tst_series, noise_level)
```

<!-- /wp:code -->

<!-- wp:code -->

``` {.wp-block-code}
# combine dtrain and dtest for preprocessing
alldata = pd.concat([Train,Test], axis=0)

trainlen = len(Train)

# convert character columns to integer
print("Label Encoding")
numeric = Train.select_dtypes(include=np.number).columns.tolist()
categorical = [f for f in Train.columns.tolist() if f not in numeric]
categorical
for cat in categorical:
    alldata[cat] = le.fit_transform(alldata[cat].fillna(alldata[cat].mode().iloc[0]))

# split back into dtrain and dtest
Train = alldata[:trainlen]
Test = alldata[trainlen:]
```

<!-- /wp:code -->

<!-- wp:heading -->

Training
--------

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:code -->

``` {.wp-block-code}
params = {
    'boosting_type' : 'gbdt', 
    'objective' : 'binary',
    'metric' : 'binary_logloss', 
    'nthread' : 16, 
    'learning_rate' : 0.02,
    'max_depth' : 12,
    'num_leaves' : 100,
    'sub_feature' : 0.7, 
    'sub_row' : 0.7, 
    'bagging_freq' : 1,
    'bagging_fraction' : 0.8,
    'lambda_l1': 0.1, 
    'lambda_l2' : 0.2
}

def modeling_cross_validation(params, X, y, folds):
    clfs = []
    allPreds = np.zeros(X.shape[0])

    evals_result = {}

    X_len = int(len(X)/3)

    X_train = X[X_len:]
    X_valid = X[:X_len]
    y_train = y[X_len:]
    y_valid = y[:X_len] 

    lgb_train = lgb.Dataset(X_train, y_train)
    lgb_valid = lgb.Dataset(X_valid, y_valid, reference=lgb_train)

    model = lgb.train(params,
                lgb_train,
                num_boost_round=200,
                valid_sets=[lgb_train, lgb_valid],
                evals_result=evals_result,
                verbose_eval=100,
                early_stopping_rounds=50)

    print('Plot metrics during training...')
    ax = lgb.plot_metric(evals_result, metric='binary_logloss')
    plt.show()

    print('Plot feature importances...')
    ax = lgb.plot_importance(model, max_num_features=10)
    plt.show()

    '''

    allPreds = model.predict(X_test)

    score = roc_auc_score(y_test, allPreds)
    print(score)
    '''

    clfs.append(model)
    return clfs


def predict_cross_validation(test, clfs):

    sub_preds = np.zeros(test.shape[0])

    for i, model in enumerate(clfs, 1):    
        test_preds = model.predict_proba(test)
        sub_preds += test_preds[:,1]

    # Averaging across all models
    sub_preds = sub_preds / len(clfs)

    # Creating a series from the predictions
    ret = pd.Series(sub_preds, index=test.index)
    ret.index.name = test.index.name 

    return ret

def predict_test_chunk(clfs, Test, filename='tmp.csv', chunks=100000):

    preds_sub = pd.DataFrame()

    num = int(7853253/100000)

    groups = Test.groupby(np.arange(len(Test))//chunks)

    count = 0

    for idx, df in groups:

        if count == 10:
            print("Running on idx {} of {}".format(idx, num))
            count = 0
        count += 1

        preds_df = predict_cross_validation(df, clfs)
        preds_df = preds_df.to_frame('HasDetections')

        preds_sub = pd.concat([preds_sub, preds_df], axis=0)

        del preds_df
        gc.collect()

    return preds_sub
```

<!-- /wp:code -->

<!-- wp:code -->

``` {.wp-block-code}
print("Start Training")
clfs = modeling_cross_validation(params, Train, y, 3)
```

<!-- /wp:code -->

<!-- wp:code -->

``` {.wp-block-code}
Start Training
Training until validation scores don't improve for 50 rounds.
[100]    training's binary_logloss: 0.626603 valid_1's binary_logloss: 0.632894
[200]    training's binary_logloss: 0.614641 valid_1's binary_logloss: 0.624013
Did not meet early stopping. Best iteration is:
[200]    training's binary_logloss: 0.614641 valid_1's binary_logloss: 0.624013
Plot metrics during training...
```

<!-- /wp:code -->

<!-- wp:code -->

``` {.wp-block-code}
Plot feature importances...
```

<!-- /wp:code -->

<!-- wp:image {"id":241} -->

<figure class="wp-block-image">
![placeholder]({attach}media/2019/01/output_9_1.png){.wp-image-241}


<!-- /wp:image -->

<!-- wp:image {"id":242} -->

<figure class="wp-block-image">
![placeholder]({attach}media/2019/01/output_9_3.png){.wp-image-242}


<!-- /wp:image -->

<!-- wp:code -->

``` {.wp-block-code}
print("Start Predicting")
preds = predict_test_chunk(clfs, Test, chunks=100000)

print("Start Submission")
df_sub = pd.read_csv('sample_submission.csv')
df_sub['HasDetections'] = preds['HasDetections'].values
df_sub.to_csv('mySubmission.csv', index=False)

print("Done!")
```

<!-- /wp:code -->
