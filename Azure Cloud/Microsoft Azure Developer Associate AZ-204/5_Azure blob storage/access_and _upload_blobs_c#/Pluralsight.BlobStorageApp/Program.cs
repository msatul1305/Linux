using Azure;
using Azure.Storage.Blobs;
using Azure.Storage.Blobs.Models;
using System;
using System.IO;
using System.Threading.Tasks;

namespace Pluralsight.BlobStorageApp
{
  class Program
  {
    // TODO: Add your connection string here
    private static readonly string _connectionString = "";

    private static readonly string _blobContainerName = "authors";
    private static readonly string _blobName = "thomas.html";

    private async static Task Main(string[] args)
    {
      try
      {
        await CreateContainerAndUploadBlobAsync();

        await ListContainersWithTheirBlobsAsync();

        await DownloadBlobAsync();

        Console.WriteLine();
        Console.WriteLine($"Press ENTER to delete blob container '{_blobContainerName}'");
        Console.ReadLine();

        await DeleteContainerAsync();
      }
      catch (RequestFailedException exception)
      {
        Console.WriteLine($"Error: {exception.ErrorCode}");

        if (exception.ErrorCode == "ContainerBeingDeleted")
        {
          Console.WriteLine($"> The container '{_blobContainerName}' is currently being deleted.");
          Console.WriteLine("> This takes usually up to 30 seconds.");
          Console.WriteLine("> Wait a bit and run the program again.");
        }
      }
      catch (Exception exception)
      {
        Console.WriteLine(exception.Message);
      }
    }

    private static async Task CreateContainerAndUploadBlobAsync()
    {
      // 1. Create the Blob Container
      BlobServiceClient blobServiceClient = new BlobServiceClient(_connectionString);

      BlobContainerClient blobContainerClient =
          blobServiceClient.GetBlobContainerClient(_blobContainerName);

      Console.WriteLine($"1. Creating blob container '{_blobContainerName}'");

      await blobContainerClient.CreateIfNotExistsAsync(PublicAccessType.BlobContainer);

      // 2. Upload a Blob
      BlobClient blobClient = blobContainerClient.GetBlobClient(_blobName);

      Console.WriteLine($"2. Uploading blob '{blobClient.Name}'");
      Console.WriteLine($"   > {blobClient.Uri}");

      using FileStream fileStream = File.OpenRead("fileToUpload.html");

      await blobClient.UploadAsync(fileStream,
        new BlobHttpHeaders { ContentType = "text/html" });
    }

    private static async Task ListContainersWithTheirBlobsAsync()
    {
      BlobServiceClient blobServiceClient = new BlobServiceClient(_connectionString);

      Console.WriteLine("3. Listing containers and blobs "
          + $"of '{blobServiceClient.AccountName}' account");

      await foreach (BlobContainerItem blobContainerItem
        in blobServiceClient.GetBlobContainersAsync())
      {
        Console.WriteLine($"   > {blobContainerItem.Name}");

        BlobContainerClient blobContainerClient =
          blobServiceClient.GetBlobContainerClient(blobContainerItem.Name);

        await foreach (BlobItem blobItem in blobContainerClient.GetBlobsAsync())
        {
          Console.WriteLine($"     - {blobItem.Name}");
        }
      }
    }

    private static async Task DownloadBlobAsync()
    {
      string localFileName = "downloaded.html";

      Console.WriteLine($"4. Downloading blob '{_blobName}' to local file '{localFileName}'");

      BlobClient blobClient = new BlobClient(_connectionString, _blobContainerName, _blobName);
      bool exists = await blobClient.ExistsAsync();
      if (exists)
      {
        BlobDownloadInfo blobDownloadInfo = await blobClient.DownloadAsync();

        using FileStream fileStream = File.OpenWrite(localFileName);
        await blobDownloadInfo.Content.CopyToAsync(fileStream);
      }
    }

    private static async Task DeleteContainerAsync()
    {
      Console.WriteLine($"5. Deleting blob container '{_blobContainerName}'");

      BlobContainerClient blobContainerClient =
          new BlobContainerClient(_connectionString, _blobContainerName);

      await blobContainerClient.DeleteIfExistsAsync();
    }
  }
}
