from unittest.mock import patch, mock_open, call

import pytest
import datetime

from subshift import main, match_n_move_times


def test_main_sub16():
    """This shows the result overlaps at the shift time. Subsequent times are
    all shifted correctly."""
    with open("tests/test_file.sbv") as f:
        insbv = f.read()
    with patch("builtins.open", mock_open(read_data=insbv)) as mocked_open:
        main(["captions.sbv", "0:00:54.020", "-16"])
    mocked_open.return_value.write.assert_has_calls([
        call('0:00:02.940,0:00:10.620\n'),
        call('Lorem ipsum dolor sit amet, consectetur\xa0\n'),
        call('adipiscing elit. Pellentesque malesuada, diam a\n'),
        call('\n'),
        call('0:00:10.620,0:00:16.200\n'),
        call('sollicitudin aliquet, ipsum justo facilisis mi,\xa0\n'),
        call('et hendrerit nunc tellus nec felis. Curabitur ac molestie nisi.\n'),
        call('\n'),
        call('0:00:16.200,0:00:20.880\n'),
        call('Proin ultrices mauris ut iaculis maximus.\xa0\n'),
        call('Suspendisse libero odio, tempor eu\n'),
        call('\n'),
        call('0:00:20.880,0:00:27.360\n'),
        call('arcu et, ultricies vehicula eros. Etiam sagittis,\xa0\n'),
        call('tellus et ultrices commodo, ligula ex laoreet leo, et rutrum\n'),
        call('\n'),
        call('0:00:27.360,0:00:34.800\n'),
        call('urna magna eu mauris. Fusce tristique\xa0\n'),
        call('pulvinar neque eu congue. Sed consectetur,\n'),
        call('\n'),
        call('0:00:34.800,0:00:41.760\n'),
        call('est ut mattis tristique, mauris tellus condimentum ipsum,\xa0\n'),
        call('vitae volutpat mauris eros et lorem. Nullam dui augue,\n'),
        call('\n'),
        call('0:00:41.760,0:00:46.380\n'),
        call('gravida ut est eget, cursus porttitor nisi. Mauris in orci\xa0\n'),
        call('ut orci bibendum ornare non sed mauris. Nulla aliquet est\n'),
        call('\n'),
        call('0:00:47.460,0:00:51.360\n'),
        call('urna eleifend ac. Etiam eleifend augue sit\xa0\n'),
        call('amet posuere ultricies. Sed auctor\n'),
        call('\n'),
        call('0:00:38.900,0:00:45.560\n'),
        call('metus vitae enim porttitor, eget faucibus\xa0\n'),
        call('diam lacinia. Maecenas pellentesque\n'),
        call('\n'),
        call('0:00:45.560,0:00:51.440\n'),
        call('diam nec mauris tempus pulvinar. Sed vel\xa0\n'),
        call('erat eget mi aliquam dapibus a ac leo. Phasellus\n'),
        call('\n'),
        call('0:00:51.440,0:00:56.360\n'),
        call('vehicula, dui non faucibus cursus, tellus\xa0\n'),
        call('nisl iaculis nulla, sed gravida ipsum\n'),
        call('\n'),
        call('0:00:56.360,0:01:05.840\n'),
        call('neque sed est. Nunc bibendum neque metus,\xa0\n'),
        call('non pretium lectus auctor eget.\n'),
        call('\n'),
        call('0:01:05.840,0:01:12.980\n'),
        call('Donec lobortis, libero ac mattis pellentesque,\xa0\n'),
        call('lectus nisi tincidunt ex, sit amet sollicitudin\n'),
        call('\n'),
        call('0:01:12.980,0:01:19.460\n'),
        call('diam orci at felis. Etiam tempor ligula\xa0\n'),
        call('et dolor ultrices auctor. Duis id dictum dui.\n'),
        call('\n'),
        call('0:01:21.080,0:01:26.600\n'),
        call('et varius.\n'),
        call('\n')
    ]
    )
    mocked_open.assert_has_calls(
        [call('captions.sbv'), call('captions-16.0.sbv', 'w')],
        any_order=True
    )


def test_main_add16():
    """This shows the result lacks text at the shift time. Subsequent times are
    all shifted correctly."""
    with open("tests/test_file.sbv") as f:
        insbv = f.read()
    with patch("builtins.open", mock_open(read_data=insbv)) as mocked_open:
        main(["captions.sbv", "0:00:54.020", "16"])
    mocked_open.return_value.write.assert_has_calls([
        call('0:00:02.940,0:00:10.620\n'),
        call('Lorem ipsum dolor sit amet, consectetur\xa0\n'),
        call('adipiscing elit. Pellentesque malesuada, diam a\n'),
        call('\n'),
        call('0:00:10.620,0:00:16.200\n'),
        call('sollicitudin aliquet, ipsum justo facilisis mi,\xa0\n'),
        call('et hendrerit nunc tellus nec felis. Curabitur ac molestie nisi.\n'),
        call('\n'),
        call('0:00:16.200,0:00:20.880\n'),
        call('Proin ultrices mauris ut iaculis maximus.\xa0\n'),
        call('Suspendisse libero odio, tempor eu\n'),
        call('\n'),
        call('0:00:20.880,0:00:27.360\n'),
        call('arcu et, ultricies vehicula eros. Etiam sagittis,\xa0\n'),
        call('tellus et ultrices commodo, ligula ex laoreet leo, et rutrum\n'),
        call('\n'),
        call('0:00:27.360,0:00:34.800\n'),
        call('urna magna eu mauris. Fusce tristique\xa0\n'),
        call('pulvinar neque eu congue. Sed consectetur,\n'),
        call('\n'),
        call('0:00:34.800,0:00:41.760\n'),
        call('est ut mattis tristique, mauris tellus condimentum ipsum,\xa0\n'),
        call('vitae volutpat mauris eros et lorem. Nullam dui augue,\n'),
        call('\n'),
        call('0:00:41.760,0:00:46.380\n'),
        call('gravida ut est eget, cursus porttitor nisi. Mauris in orci\xa0\n'),
        call('ut orci bibendum ornare non sed mauris. Nulla aliquet est\n'),
        call('\n'),
        call('0:00:47.460,0:00:51.360\n'),
        call('urna eleifend ac. Etiam eleifend augue sit\xa0\n'),
        call('amet posuere ultricies. Sed auctor\n'),
        call('\n'),
        call('0:01:10.900,0:01:17.560\n'),
        call('metus vitae enim porttitor, eget faucibus\xa0\n'),
        call('diam lacinia. Maecenas pellentesque\n'),
        call('\n'),
        call('0:01:17.560,0:01:23.440\n'),
        call('diam nec mauris tempus pulvinar. Sed vel\xa0\n'),
        call('erat eget mi aliquam dapibus a ac leo. Phasellus\n'),
        call('\n'),
        call('0:01:23.440,0:01:28.360\n'),
        call('vehicula, dui non faucibus cursus, tellus\xa0\n'),
        call('nisl iaculis nulla, sed gravida ipsum\n'),
        call('\n'),
        call('0:01:28.360,0:01:37.840\n'),
        call('neque sed est. Nunc bibendum neque metus,\xa0\n'),
        call('non pretium lectus auctor eget.\n'),
        call('\n'),
        call('0:01:37.840,0:01:44.980\n'),
        call('Donec lobortis, libero ac mattis pellentesque,\xa0\n'),
        call('lectus nisi tincidunt ex, sit amet sollicitudin\n'),
        call('\n'),
        call('0:01:44.980,0:01:51.460\n'),
        call('diam orci at felis. Etiam tempor ligula\xa0\n'),
        call('et dolor ultrices auctor. Duis id dictum dui.\n'),
        call('\n'),
        call('0:01:53.080,0:01:58.600\n'),
        call('et varius.\n'),
        call('\n'),
    ]
    )
    mocked_open.assert_has_calls(
        [call('captions.sbv'), call('captions16.0.sbv', 'w')],
        any_order=True
    )

@pytest.mark.parametrize("pivot, recorded, delta_s, new_line", [
    ("0:01:43.920", "0:01:43.920,0:01:49.740", 45, "0:01:43.920,0:01:49.740"),
    ("0:01:42.920", "0:01:43.920,0:01:49.740", -45, "0:00:58.920,0:01:04.740"),
    ("0:01:42.920", "0:01:43.920,0:01:49.740", 45, "0:02:28.920,0:02:34.740"),
])
def test_match_n_move_times(pivot, recorded, delta_s, new_line):
    pivot_time = datetime.datetime.strptime(pivot, "%H:%M:%S.%f")
    assert new_line == match_n_move_times(
        pivot_time, recorded, datetime.timedelta(seconds=delta_s))
