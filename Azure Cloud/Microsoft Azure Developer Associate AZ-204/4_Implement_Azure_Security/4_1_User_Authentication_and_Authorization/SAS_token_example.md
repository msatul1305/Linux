URL https://storagename.blob.core.windows.nety?
signedVersion sv=2019-12-12&
signedServices ss=bfqt& [signed service for blob, file, queue and table]
signedResourceType srt=s&
signedPermission sp=rwdlacupx&  [read, write, delete, list(rwdla), create, update, process]
signedExpiry  se=202..&
Signed Start st=date&
signedProtocol spr=https&
signature sig=dXxxXko;lawedkjlbhqwbewhikjvbrfklb%3d%3D

More details on parameters: https://docs.microsoft.com/en-us/rest/api/storageservices/create-account-sas 
Signature = HMAC computed over string to sign + key using SHA-256 algo + encoding in Base64
if key changes, signature will change.



[//]: # (Stored access policy example:)
URL https://storagename.blob.core.windows.nety?
signedResource sr=c&
si=mypolicy&
signature sig=dXxxXko;lawedkjlbhqwbewhikjvbrfklb%3d%3D

- mypolicy contains all data like st, spr, ss, sp etc.