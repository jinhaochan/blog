Title: Microsoft Kaggle Challenge: Adversarial Validation
Date: 2019-03-10 19:45
Author: jinhaochan
Category: Data Science
Tags: Adversarial Validation
Slug: microsoft-kaggle-challenge-adversarial-validation
Status: published

<!-- wp:heading {"level":3} -->

### Overview





------------------------------------------------------------------------



</p>


This was a concept I came across while doing a Kaggle challenge issued by Microsoft to predict if a computer would get hit by a malware or not.





This challenge was different from their previous one, where they wanted you to predict if the malware class of a given binary.





This challenge was really interesting, because we had a lot of given information about the target machine, the list of them are:





`MachineIdentifier, ProductName, EngineVersion, AppVersion, AvSigVersion, IsBeta, RtpStateBitfield, IsSxsPassiveMode, DefaultBrowsersIdentifier, AVProductStatesIdentifier, AVProductsInstalled, AVProductsEnabled, HasTpm, CountryIdentifier, CityIdentifier', OrganizationIdentifier', GeoNameIdentifier', LocaleEnglishNameIdentifier', Platform', Processor', OsVer', OsBuild', OsSuite', OsPlatformSubRelease', OsBuildLab', SkuEdition', IsProtected', AutoSampleOptIn', PuaMode', SMode', IeVerIdentifier', SmartScreen', Firewall', UacLuaenable', Census_MDC2FormFactor', Census_DeviceFamily', Census_OEMNameIdentifier', Census_OEMModelIdentifier', Census_ProcessorCoreCount', Census_ProcessorManufacturerIdentifier', Census_ProcessorModelIdentifier', Census_ProcessorClass', Census_PrimaryDiskTotalCapacity', Census_PrimaryDiskTypeName', Census_SystemVolumeTotalCapacity', Census_HasOpticalDiskDrive', Census_TotalPhysicalRAM', Census_ChassisTypeName', Census_InternalPrimaryDiagonalDisplaySizeInInches', Census_InternalPrimaryDisplayResolutionHorizontal', Census_InternalPrimaryDisplayResolutionVertical', Census_PowerPlatformRoleName', Census_InternalBatteryType', Census_InternalBatteryNumberOfCharges', Census_OSVersion', Census_OSArchitecture', Census_OSBranch', Census_OSBuildNumber', Census_OSBuildRevision', Census_OSEdition', Census_OSSkuName', Census_OSInstallTypeName', Census_OSInstallLanguageIdentifier', Census_OSUILocaleIdentifier', Census_OSWUAutoUpdateOptionsName', Census_IsPortableOperatingSystem', Census_GenuineStateName', Census_ActivationChannel', Census_IsFlightingInternal', Census_IsFlightsDisabled', Census_FlightRing', Census_ThresholdOptIn', Census_FirmwareManufacturerIdentifier', Census_FirmwareVersionIdentifier', Census_IsSecureBootEnabled', Census_IsWIMBootEnabled', Census_IsVirtualDevice', Census_IsTouchEnabled', Census_IsPenCapable, Census_IsAlwaysOnAlwaysConnectedCapable, Wdft_IsGamer, Wdft_RegionIdentifier`





Now that's pretty crazy, with things like Screen size, is the PC build a gaming PC or not, and is touch screen enabled. With such complex features, it'll be really challenging to pick out patterns to predict if the machine will get hit or not.





But one important thing that stood out was how different the test set was compared to the training set. This can be shown in the following way:



<!-- wp:list {"ordered":true} -->

1.  Random sample 10k rows from the training data set and the testing data set
2.  Drop the initial label (in this case, `HasDetected`), and put in your own label `IsTrain` , and give the training data 1, and the test data 0
3.  Build a classifier to predict if a given row came from the training data set, or the testing data set
4.  If the model gives a high accuracy, it means that the training and testing data are really different.
5.  If the model gives an accuracy of about 50%, it means that the training and testing data are almost the same





The model I built was LightGBM, and it gave me an incredible score of 93%! That means that the training and testing data set are incredibly different.





This gives us some problems if we use the standard solution of cross validation of the training data, since at the end, the testing data is so disparate.



<!-- wp:heading {"level":3} -->

### Adversarial Validation





------------------------------------------------------------------------



</p>


In comes adversarial validation. The idea of this actually really simple.





Based on the model we built earlier to classify is a row belongs to training or testing, we use the same model to run the classification only on the training data set.





We then pick out the rows that the model identified wrongly as testing data. This means that those rows inside the training data set have features that are similar to the testing data set!





And so, instead of the conventional validation methods, we use these rows classified falsely as testing to be our validation data. This way, our model validates itself to data that is close the testing data, and there would not have a huge difference in performance when training the model, and testing it.



<!-- wp:heading {"level":3} -->

### Downside





------------------------------------------------------------------------



</p>


One of the downsides of doing this is that, once the testing data set changes again to something that is dissimilar to the current data, we the adversarial validation technique would perform poorly again.





This might mean that we need to retrain the adversarial data selection model, and pick out falsely classified rows, and retrain the prediction model all over again. And that sounds like a lot of work.


