import React, { FunctionComponent, createRef } from 'react';
import { StyleSheet, View, Dimensions, TextInput } from 'react-native';
import {
  Container,
  Text,
  Content,
  Form,
  Item,
  Input,
  Icon,
  Button,
} from 'native-base';
import { StackNavigationProp } from '@react-navigation/stack';
import { RootStackParamList } from '../App';
import { ip } from '../Secure';

type LoginProps = {
  navigation: StackNavigationProp<RootStackParamList, 'Login'>;
};

const Login: FunctionComponent<LoginProps> = (props: LoginProps) => {
  const [username, setUsername] = React.useState<string>('');
  const [password, setPassword] = React.useState<string>('');
  const [usernameError, setUsernameError] = React.useState<string>('');
  const [passwordError, setPasswordError] = React.useState<string>('');

  function loginRequest() {
    fetch(`http://${ip}:8000/api/token`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ username: username, password: password }),
    })
      .then((response: Response) => response.json())
      .then((result: JSON) => {
        console.log(result);
      })
      .catch((reason: any) => console.log(reason));
  }

  return (
    <Container>
      <Content padder>
        <Form>
          <View style={styles.textInputsView}>
            <View style={styles.titleView}>
              <Text style={styles.title}>Reinvented Checkers</Text>
            </View>
            <View style={styles.paddedItem}>
              <Item
                error={usernameError.length > 0}
                rounded
                style={styles.item}
              >
                <Input
                  style={styles.input}
                  placeholder={
                    usernameError.length > 0 ? usernameError : 'Username'
                  }
                  autoCapitalize="none"
                  onChangeText={(text: string) => {
                    setUsernameError('');
                    setUsername(text);
                  }}
                  enablesReturnKeyAutomatically
                  returnKeyType="done"
                />
                {usernameError.length > 0 && (
                  <Icon style={styles.icon} name="close-circle" />
                )}
              </Item>
            </View>
            <View style={styles.paddedItem}>
              <Item
                error={passwordError.length > 0}
                rounded
                style={styles.item}
              >
                <Input
                  style={styles.input}
                  placeholder="Password"
                  autoCapitalize="none"
                  secureTextEntry={true}
                  onChangeText={(text: string) => {
                    setPassword(text);
                  }}
                  enablesReturnKeyAutomatically
                  returnKeyType="done"
                />
              </Item>
            </View>
          </View>
          <View style={styles.paddedItem}>
            <Button
              rounded
              info
              block
              style={styles.item}
              onPress={() => {
                loginRequest();
              }}
            >
              <Text style={styles.buttonText}>Login</Text>
            </Button>
          </View>
          <View style={styles.paddedItem}>
            <Button
              rounded
              warning
              block
              style={styles.item}
              onPress={() => props.navigation.navigate('Home')}
            >
              <Text style={styles.buttonText}>Sign Up</Text>
            </Button>
          </View>
        </Form>
      </Content>
    </Container>
  );
};

const styles = StyleSheet.create({
  titleView: { paddingVertical: 75 },
  title: { textAlign: 'center', fontSize: 30 },
  textInputsView: { height: Math.round(Dimensions.get('window').height) - 200 },
  item: { height: 55 },
  paddedItem: { paddingBottom: 20 },
  input: { fontSize: 16, paddingLeft: 20 },
  icon: { paddingRight: 20 },
  buttonText: { fontSize: 16 },
});

export default Login;
