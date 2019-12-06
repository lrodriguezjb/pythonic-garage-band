import pytest
from pythonic_garage_band import Band, Musician, Guitarist, Bassist, Drummer, Singer


def do_you_wanna_rock():
    assert "Are you ready for some kick-ass solos?" == Band.moment_of_fame()


def test_Dave_is_instance_of_correct_class(Leandro):
    assert isinstance(Leandro, Singer)


def test_Dave_is_instance_of_parent_class(Leandro):
    assert isinstance(Leandro, Musician)


def test_jimmy_name(Leandro):
    assert Leandro.name == 'Leandro'


def test_Dave_instrument(Leandro):
    assert Leandro.instrument == 'Vocals'


# def test_to_list():
#     Leandro = Singer('Leandro', 'Vocals')
#     Rafael = Guitarist('Rafael', 'guitar')
#     Alfonso = Bassist('Alfonso', 'bass')
#     Matt = Drummer('Matt', 'drums')
#     expected = [Leandro, Rafael, Alfonso, Matt]
#     actual = Band.to_list()
#     assert actual == expected


# def test_create_band_from_data(Leandro):
#     data = [
#         {'name': 'Leandro',
#          'instrument': 'Vocals'
#          },
#         {'name': 'Alfonso',
#          'instrument': 'Bass'
#          },
#         {'name': 'Matt',
#          'instrument': 'Drums'
#          },
#         {'name': 'Rafael',
#          'instrument': 'Guitar'
#          }
#     ]
#     Band.create_from_data(data)

#     assert Band.members[0] == Leandro


@pytest.fixture()
def Leandro():
    return Singer('Leandro', 'Vocals')


@pytest.fixture(autouse=True)
def clean():
    Band.members = []
