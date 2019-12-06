import click

from ..login import cluster_call
from ..utils import global_options


@click.group(short_help='info, list',
             epilog='Type "ae5 endpoint <command> --help" for help on a specific command.')
@global_options
def endpoint():
    '''Commands related to static endpoints.'''
    pass


@endpoint.command()
@global_options
def list():
    '''List the static endpoints on this cluster.
    '''
    cluster_call('endpoint_list', cli=True)


@endpoint.command()
@click.argument('endpoint')
@global_options
def info(endpoint):
    '''Retrieve the record of a single endpoint.

       The ENDPOINT identifier need not be fully specified, and may even include
       wildcards. But it must match exactly one endpoint name or ID.
    '''
    cluster_call('endpoint_info', endpoint, cli=True)
