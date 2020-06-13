import React, { FunctionComponent } from 'react';
import { StyleSheet, View } from 'react-native';
import {
  Container,
  Text,
  Content,
  Form,
  Item,
  Input,
  Button,
} from 'native-base';

type LoginProps = {};

const Login: FunctionComponent<LoginProps> = (props: LoginProps) => {
  return (
    <Container>
      <Content padder>
        <Form>
          <View style={styles.titleView}>
            <Text style={styles.title}>Reinvented Checkers</Text>
          </View>
          <View style={styles.textInputsView}>
            <View style={styles.paddedItem}>
              <Item rounded style={styles.item}>
                <Input
                  style={styles.input}
                  placeholder="Username"
                  autoCapitalize="none"
                />
              </Item>
            </View>
            <View style={styles.paddedItem}>
              <Item rounded style={styles.item}>
                <Input
                  style={styles.input}
                  placeholder="Password"
                  autoCapitalize="none"
                  secureTextEntry={true}
                />
              </Item>
            </View>
          </View>
          <View style={styles.paddedItem}>
            <Button rounded info block style={styles.item}>
              <Text style={styles.buttonText}>Login</Text>
            </Button>
          </View>
          <View style={styles.paddedItem}>
            <Button rounded warning block style={styles.item}>
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
  textInputsView: { paddingBottom: 75 },
  item: { height: 55 },
  paddedItem: { paddingBottom: 20 },
  input: { fontSize: 16, paddingLeft: 20 },
  buttonText: { fontSize: 16 },
});

export default Login;
