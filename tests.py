from click.testing import CliRunner

from hide_env import hide_env


def test_hide_env_should_replace_variable_with_placeholder(monkeypatch, mocker):
    runner = CliRunner()
    monkeypatch.setenv('SECRET', '42')
    result = runner.invoke(hide_env, ['SECRET'], input='somevalue 42 is secret')

    assert not result.exception
    assert result.output == 'somevalue [SECRET] is secret'
