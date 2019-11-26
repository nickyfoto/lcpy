from click.testing import CliRunner
from lcpy.cli import lcpy_cp

def test_sync():
  runner = CliRunner()
  result = runner.invoke(lcpy_cp, ['some.py'])
  assert result.exit_code == 0
  assert 'some.py' in result.output
