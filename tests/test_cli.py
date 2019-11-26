from click.testing import CliRunner
from lcpy.cli import cp

def test_sync():
  runner = CliRunner()
  result = runner.invoke(cp, ['some.py'])
  assert result.exit_code == 0
  assert 'some.py' in result.output
