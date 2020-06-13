import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import { AppLoading } from 'expo';
import * as Font from 'expo-font';
import { Ionicons } from '@expo/vector-icons';
import { Button, Text } from 'native-base';
import Home from './components/Home';
import Login from './components/Login';

export default function App() {
  const [isReady, setIsReady] = React.useState<boolean>(false);
  React.useEffect(() => {
    Font.loadAsync({
      Roboto: require('native-base/Fonts/Roboto.ttf'),
      Roboto_medium: require('native-base/Fonts/Roboto_medium.ttf'),
      ...Ionicons.font,
    });
    setIsReady(true);
  }, []);
  if (!isReady) {
    return <AppLoading />;
  }
  const Stack = createStackNavigator();
  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen
          name="Login"
          component={Login}
          options={{ headerShown: false }}
        />
        <Stack.Screen
          name="Home"
          component={Home}
          options={{
            title: 'Hello',
            headerRight: () => (
              <Button
                transparent
                onPress={() => alert('This is a button!')}
                color="#fff"
              >
                <Text>Header</Text>
              </Button>
            ),
          }}
        />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
