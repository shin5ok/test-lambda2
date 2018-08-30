import json
import datetime
import boto3

client = None
bucket_name = "serverless-handson-kawano"

def handler(event, context):

    global client
    if not client:
        client = boto3.resource('s3')
    objects = []
    try:
        for f in client.Bucket(bucket_name).objects.all():
            objects.append(f.key)
            # objects.append(str(f))

        data = {
            'output': 'Hello World',
            'events': event,
            'context': context,
            'timestamp': datetime.datetime.utcnow().isoformat(),
            'objects': objects
        }
    except:
        pass
    rdata ={'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
    print(rdata)
    return rdata

# print(handler({}, {}))

# if __name__ == '__main__':
#     print(handler(None, None))

#            >>> boto3.resource('s3')
#            s3.ServiceResource()
#            >>> v=boto3.resource('s3')
#            >>> v.Bucket('kawano-backup')
#            s3.Bucket(name='kawano-backup')
#            >>> vv=v.Bucket('kawano-backup')
#            >>> dir(vv)
#            [u'Acl', u'Cors', u'Lifecycle', u'LifecycleConfiguration', u'Logging', u'Notification', u'Object', u'Policy', u'RequestPayment', u'Tagging', u'Versioning', u'Website', '__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_name', 'copy', u'create', u'creation_date', u'delete', u'delete_objects', 'download_file', 'download_fileobj', 'get_available_subresources', 'load', 'meta', u'multipart_uploads', u'name', u'object_versions', u'objects', u'put_object', 'upload_file', 'upload_fileobj', u'wait_until_exists', u'wait_until_not_exists']
#            >>> vv.object.all()
#            Traceback (most recent call last):
#              File "<stdin>", line 1, in <module>
#              AttributeError: 's3.Bucket' object has no attribute 'object'
#              >>> vv.objects.all()
#              s3.Bucket.objectsCollection(s3.Bucket(name='kawano-backup'), s3.ObjectSummary)
#              >>> for vvv in vv.objects.all():
#              ...     print(vvv)
#              ...
#              s3.ObjectSummary(bucket_name='kawano-backup', key=u'services')
#              >>> for vvv in vv.objects.all():
#              ...     print(vvv.key)
#              ...
#              services
