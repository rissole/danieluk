chmod +x *.sh
python config.py
echo
echo
echo "Installing dependencies....";
echo "Just type your sudo password, it's fiiiiiiiiiiiiine....";
sudo easy_install pip;
sudo pip install flask;
echo
echo
echo
echo "Done!"
echo "RECOMMENDED: Settings > Dictation and Speech > System Voice > Customze > UK > Daniel"
echo
echo "Run ./start.sh to start the server so people can contact you"
