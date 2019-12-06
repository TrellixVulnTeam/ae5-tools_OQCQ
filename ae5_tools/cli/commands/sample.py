import click

from ..login import cluster_call
from ..utils import global_options


@click.group(short_help='info, list',
             epilog='Type "ae5 project sample <command> --help" for help on a specific command.')
@global_options
def sample():
    '''Commands related to sample and template projects.'''
    pass


@sample.command()
@global_options
def list():
    '''List the sample projects.
    '''
    cluster_call('sample_list', cli=True)


@sample.command()
@click.argument('project')
@global_options
def info(project):
    '''Retrieve the record of a single sample project.

       The PROJECT identifier must match exactly one name or id of a sample project.
       Wildcards may be included.
    '''
    cluster_call('sample_info', project, cli=True)


@sample.command()
@click.argument('project')
@click.option('--name', type=str, required=False, help='Name for the job. If supplied, the name must not be identical to an existing job or run record, unless --make-unique is supplied. If not supplied, a unique name will be autogenerated from the project name.')
@click.option('--make-unique', is_flag=True, default=None, help='If supplied, a counter will be appended to a supplied --name if needed to make it unique.')
@click.option('--tag', default='', help='Commit tag to use for initial revision of project.')
@click.option('--no-wait', is_flag=True, help='Do not wait for the creation seesion to complete before exiting.')
@global_options
def clone(project, name, tag, make_unique, no_wait):
    '''Create a copy of a sample or template project.

       The PROJECT identifier must match exactly one name or id of a sample project.
       Wildcards may be included.
    '''
    cluster_call('sample_clone', project, name=name, tag=tag,
                 make_unique=make_unique, wait=not no_wait, cli=True)
