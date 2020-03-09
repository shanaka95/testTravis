import libtorrent as lt
import time

ses = lt.session()
ses.listen_on(6881, 6891)
params = {
    'save_path': './',
    'storage_mode': lt.storage_mode_t(2),
    'paused': False,
    'auto_managed': True,
    'duplicate_is_error': True}
link = "magnet:?xt=urn:btih:9071426B5A6D7C9873B4B9062601B81E3EC6DB42&dn=Sonic.the.Hedgehog.2020.1080p.HDRip.X264.AC3-EVO%5BTGx%5D+%E2%AD%90&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&tr=udp%3A%2F%2Fexodus.desync.com%3A6969&tr=udp%3A%2F%2Fp4p.arenabg.com%3A1337%2Fannounce&tr=udp%3A%2F%2Fexplodie.org%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.tiny-vps.com%3A6969%2Fannounce&tr=udp%3A%2F%2Fopen.demonii.si%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.torrent.eu.org%3A451%2Fannounce&tr=udp%3A%2F%2Ftracker.pirateparty.gr%3A6969%2Fannounce&tr=udp%3A%2F%2Fipv4.tracker.harry.lu%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.cyberia.is%3A6969%2Fannounce&tr=udp%3A%2F%2F9.rarbg.to%3A2710%2Fannounce&tr=udp%3A%2F%2Ftracker.zer0day.to%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&tr=udp%3A%2F%2Fcoppersurfer.tk%3A6969%2Fannounce"
handle = lt.add_magnet_uri(ses, link, params)
ses.start_dht()

print 'downloading metadata...'
while (not handle.has_metadata()):
    time.sleep(1)
print 'got metadata, starting torrent download...'
while (handle.status().state != lt.torrent_status.seeding):
    s = handle.status()
    state_str = ['queued', 'checking', 'downloading metadata', \
            'downloading', 'finished', 'seeding', 'allocating']
    print '%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % \
            (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, \
            s.num_peers, state_str[s.state])
    time.sleep(5)
